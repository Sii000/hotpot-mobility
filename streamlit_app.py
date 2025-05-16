import streamlit as st

st.set_page_config(page_title="ActivityFinder", layout="centered")

# Initiera första sidan
if "page" not in st.session_state:
    st.session_state.page = "home"

# Funktion för att byta sida
def navigate_to(page):
    st.session_state.page = page
    st.rerun()

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
    right: 0;
    height: 70px;
    background-color: white;
    border-top: 1px solid #ddd;
    display: flex;
    justify-content: space-around;
    align-items: center;
    z-index: 1000;
}
.bottom-nav button {
    background: none;
    border: none;
    font-size: 18px;
    color: #444;
    cursor: pointer;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 4px;
    padding: 0;
}
.bottom-nav button.selected {
    color: #007bff;
    font-weight: bold;
}
.block-container {
    padding-bottom: 80px;
}
</style>
""", unsafe_allow_html=True)

# Bottenmeny i ren HTML via Streamlit knappar i flexbox
col1, col2, col3 = st.columns([1,1,1])
with col1:
    if st.button("🏠\nStartsida", key="home_btn"):
        navigate_to("home")
with col2:
    if st.button("🗺️\nKarta", key="map_btn"):
        navigate_to("map")
with col3:
    if st.button("ℹ️\nOm", key="info_btn"):
        navigate_to("info")

st.markdown('</div>', unsafe_allow_html=True)
