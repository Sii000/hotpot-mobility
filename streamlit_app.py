import streamlit as st

st.set_page_config(page_title="ActivityFinder", layout="centered")

# Hämta valt menyval från session state eller default
if "page" not in st.session_state:
    st.session_state.page = "home"

def set_page(page):
    st.session_state.page = page
    

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
    align-items: center;
    padding: 0.5rem 0;
    z-index: 9999;
    box-shadow: 0 -1px 5px rgba(0,0,0,0.1);
}
.bottom-nav button {
    background: none;
    border: none;
    font-size: 14px;
    color: #444;
    cursor: pointer;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 4px;
    padding: 6px 12px;
    min-width: 60px;
    transition: color 0.3s;
}
.bottom-nav button.selected {
    color: #0066cc;
    font-weight: bold;
}
.block-container {
    padding-bottom: 80px;
}
</style>
""", unsafe_allow_html=True)


# Bottenmeny med knappar och ikoner + text
with st.container():
    st.markdown('<div class="bottom-nav">', unsafe_allow_html=True)
    cols = st.columns(3)
    with cols[0]:
        if st.button("🏠\nStartsida", key="btn_home", help="Startsida", 
                     on_click=set_page, args=("home",)):
            pass
    with cols[1]:
        if st.button("🗺️\nKarta", key="btn_map", help="Karta", 
                     on_click=set_page, args=("map",)):
            pass
    with cols[2]:
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

