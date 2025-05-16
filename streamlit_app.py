import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="ActivityFinder", layout="wide")

st.markdown("<div style='padding-bottom: 70px;'></div>", unsafe_allow_html=True)


# Initiera session state
if "page" not in st.session_state:
    st.session_state.page = "home"

def navigate_to(page):
    st.session_state.page = page
    st.rerun()


# Använd option_menu för bottenmeny (horisontell)
selected = option_menu(
    menu_title = None,  # Ingen titel på menyn
    options = ["Startsida", "Poäng", " Karta", "Om"],
    icons = ["house", "trophy", "map", "info-circle"],
    menu_icon = "cast",
    default_index = 0,
    orientation = "horizontal",
    styles = {
        "container": {
            "padding": "0!important",
            "background-color": "#f0f0f0",
            "position": "fixed",       # fixerar menyn
            "bottom": "0",             # placerar den längst ner
            "width": "100%",           # full bredd
            "z-index": "9999",         # ligger över annat innehåll
            "border-top": "1px solid #ccc",
        },
        "nav-link": {
            "font-size": "16px",
            "text-align": "center",
            "margin": "0px",
            "--hover-color": "#eee",
        },
        "nav-link-selected": {
            "background-color": "#0d6efd",
            "color": "white",
        },
    }
)

# Spara valet i session_state
if selected == "Startsida":
    st.session_state.page = "home"
elif selected == "Poäng":
    st.session_state.page = "points"
elif selected == "Karta":
    st.session_state.page = "map"
elif selected == "Om":
    st.session_state.page = "info"

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