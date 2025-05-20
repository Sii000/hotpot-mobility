import streamlit as st
from streamlit_option_menu import option_menu


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
        "container": {"padding": "0!important", "background-color": "#f0f0f0"},
        "nav-link": {"font-size": "16px", "text-align": "center", "margin": "0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#0d6efd", "color": "white"},
        
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
    st.subheader ("Hitta pågående evenemang:")
    start_date = st.date_input("Startdatum", value=None, key="start")
    end_date = st.date_input("Slutdatum", value=None, key="end")
    data = None


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
