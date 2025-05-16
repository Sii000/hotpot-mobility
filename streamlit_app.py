import streamlit as st

st.set_page_config(page_title="ActivityFinder", layout="centered")

# CSS för att fixa bottenmeny
st.markdown("""
<style>
.bottom-nav {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background-color: #f0f0f0;
    border-top: 1px solid #ccc;
    display: flex;
    justify-content: space-around;
    padding: 0.5rem 0;
    z-index: 9999;
}
.bottom-nav button {
    background: none;
    border: none;
    font-size: 16px;
    color: #444;
    cursor: pointer;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 2px;
    padding: 0 10px;
}
.bottom-nav button.selected {
    color: #0066cc;
    font-weight: bold;
}
.block-container {
    padding-bottom: 80px; /* plats för bottenmeny */
}
</style>
""", unsafe_allow_html=True)

# Hämta valt menyval från session state eller default
if "page" not in st.session_state:
    st.session_state.page = "home"

def set_page(page):
    st.session_state.page = page

# Bottenmeny med knappar och ikoner + text
with st.container():
    st.markdown('<div class="bottom-nav">', unsafe_allow_html=True)
    cols = st.columns(3)
    with cols[0]:
        selected = st.session_state.page == "home"
        if st.button("🏠\nStartsida", key="btn_home", help="Startsida", 
                     on_click=set_page, args=("home",)):
            pass
    with cols[1]:
        selected = st.session_state.page == "map"
        if st.button("🗺️\nKarta", key="btn_map", help="Karta", 
                     on_click=set_page, args=("map",)):
            pass
    with cols[2]:
        selected = st.session_state.page == "info"
        if st.button("ℹ️\nOm", key="btn_info", help="Om", 
                     on_click=set_page, args=("info",)):
            pass
    st.markdown('</div>', unsafe_allow_html=True)

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

