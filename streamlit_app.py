import streamlit as st
from streamlit_option_menu import option_menu
from kalendarium_api import fetch_kalendarium   # pyright: ignore[reportMissingImports]


st.set_page_config (page_title = "ActivityFinder", layout = "centered")

# Initiera session state
if "page" not in st.session_state:
    st.session_state.page = "home"

def navigate_to (page):
    st.session_state.page = page
    st.rerun()
    
# Mappa interna sidnamn till menyetiketter
page_to_option = {
    "home": "Startsida",
    "points": "Poäng",
    "map": "Karta",
    "info": "Om"
}

option_to_page = {v: k for k, v in page_to_option.items()}

# Räkna ut vilket index som ska vara aktivt i menyn
default_index = list (
    page_to_option.values()).index (page_to_option.get(st.session_state.page, "Startsida"))


# Visa lite extra utrymme för bottenmenyn
st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)    

# Använd option_menu för bottenmeny (horisontell)
selected = option_menu(
    menu_title = None,  # Ingen titel på menyn
    options = ["Startsida", "Poäng", "Karta", "Om"],
    icons = ["house", "trophy", "map", "info-circle"],
    menu_icon = "cast",   
    default_index = list(page_to_option.values()).index(page_to_option[st.session_state.page]),
    orientation = "horizontal",
    styles = {
        "container": {
            "padding": "0!important", 
            "background-color": "#f0f0f0",
            "position": "fixed",
            "bottom": "0",
            "width": "100%",
            "z-index": "9999",
            "border-top": "1px solid #ccc"
        },
        "icon": {
            "display": "block",
            "margin": "0 auto",
            "font-size": "20px"
            
        },
        "nav-link": {
            "display": "flex",
            "flex-direction": "column",
            "align-items": "center",
            "font-size": "14px", 
            "margin": "0px", 
            "padding": "6px 0",
            "--hover-color": "#eee"
            
        },
        "nav-link-selected": {
            "background-color": "#0d6efd", 
            "color": "white",
            "font-weight": "bold"
        },
        
    }
)

# Uppdatera session_state beroende på användarens val
if selected and option_to_page[selected] != st.session_state.page:
    st.session_state.page = option_to_page[selected]
    st.rerun()
    

page_to_option = {
    "home": "Startsida",
    "points": "Poäng",
    "map": "Karta",
    "info": "Om"
}
    
# Visa vald sida
page = st.session_state.page

if page == "home":
    st.title("Välkommen till ActivityFinder 👋")
    st.markdown("""
    Här kommer du kunna:
    - Hitta aktiviteter i Göteborg  
    - Filtrera efter datum, plats och kategori  
    - Spara dina favoriter (kommer snart)

    Appen är anpassad för mobil – lägg till den på din hemskärm för snabb åtkomst!
    """)
    
     # Välj datumintervall
    st.title ("Hitta pågående evenemang:")
    start_date = st.date_input("Startdatum", value=None, key="start")
    end_date = st.date_input("Slutdatum", value=None, key="end")
    data = None

    if start_date and end_date:
        data = fetch_kalendarium(start_date, end_date)
        
        st.write("🔍 API-svar:")
        st.write(data)  # eller print(data) om du kör i terminalen

    if isinstance(data, list):
        for aktivitet in data:
            if isinstance(aktivitet, dict):
                st.write(f"🗓️ {aktivitet.get('title', 'Ingen titel')}")
            else:
                st.warning(f"❗ Aktivitet är inte ett dict: {aktivitet}")
    else:
        st.error("❌ API-svaret är inte en lista av aktiviteter.")



elif page == "points":
    st.title("Poäng")
    st.info("Denna funktion är inte aktiv ännu. Kommer snart!")
    
    
elif page == "map":
    st.title("Karta")
    st.info("Denna funktion är inte aktiv ännu. Kommer snart!")

elif page == "info":
    st.title("Om appen")
    st.markdown("""
    Denna app är utvecklad för att göra det enkelt att upptäcka och planera evenemang i Göteborg.

    🛠️ Utvecklad med: [Streamlit](https://streamlit.io)  
    📱 Designad för: mobilanvändning  
    """)

# OBS! OptionMenu placerar sig automatiskt längst ner om du placerar den sist i din fil
