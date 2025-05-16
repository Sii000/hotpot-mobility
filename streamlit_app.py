from streamlit import experimental_rerun
import streamlit as st


st.set_page_config(page_title="ActivityFinder", layout="centered")

# Initiera första sidan
if "page" not in st.session_state:
    st.session_state.page = "home"

# Funktion för att byta sida
def navigate_to(page):
    st.session_state.page = page

# Sidhållare
page = st.session_state.page

# 💡 SIDINNEHÅLL
if page == "home":
    st.title("Välkommen till ActivityFinder 👋")
    st.markdown("""
    Här kommer du kunna:
    - Hitta aktiviteter i Göteborg  
    - Filtrera efter datum, plats och kategori  
    - Spara dina favoriter (kommer snart)

    Appen är anpassad för mobil – lägg till den på din hemskärm för snabb åtkomst!
    """)

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

# CSS + MENY
st.markdown("""
    <style>
    .bottom-nav {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #ffffff;
        border-top: 1px solid #ddd;
        display: flex;
        justify-content: space-around;
        align-items: center;
        padding: 10px 0;
        font-size: 14px;
        z-index: 10000;
    }
    .nav-button {
        background: none;
        border: none;
        font-size: 16px;
        color: #444;
        text-align: center;
        cursor: pointer;
        flex-grow: 1;
    }
    .nav-button.selected {
        color: #0066cc;
        font-weight: bold;
    }
    .block-container {
        padding-bottom: 80px;
    }
    </style>
""", unsafe_allow_html=True)

# ⬇️ Bottenmeny med knappar
st.markdown('<div class="bottom-nav">', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🏠\nStartsida"):
        navigate_to("home")
        experimental_rerun()

with col2:
    if st.button("🗺️\nKarta"):
        navigate_to("map")
        experimental_rerun()

with col3:
    if st.button("ℹ️\nOm"):
        navigate_to("info")
        experimental_rerun()

st.markdown('</div>', unsafe_allow_html=True)
