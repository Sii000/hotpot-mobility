import streamlit as st

st.set_page_config(page_title="ActivityFinder", layout="centered")

# Hämta valt menyval från session state eller default
if "page" not in st.session_state:
    st.session_state.page = "home"

def set_page(page):
    st.session_state.page = page
    
# Hantera knapptryck (från formuläret i HTML-menyn)
if st.session_state.get("nav_submit"):
    st.session_state.page = st.session_state.nav_submit
elif st.requested_url_params.get("nav"):
    st.session_state.page = st.requested_url_params["nav"]


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
    font-size: 14px
    z-index: 10000;
}
    .nav-item.selected {
        color: #0066cc;
        font-weight: bold;
    }
    </style>

    <div class="bottom-nav">
        <form method="post">
            <button name="nav" value="home" class="nav-item {home_selected}">🏠<br>Startsida</button>
            <button name="nav" value="map" class="nav-item {map_selected}">🗺️<br>Karta</button>
            <button name="nav" value="info" class="nav-item {info_selected}">ℹ️<br>Om</button>
        </form>
    </div>
""".format(
    home_selected="selected" if st.session_state.page == "home" else "",
    map_selected="selected" if st.session_state.page == "map" else "",
    info_selected="selected" if st.session_state.page == "info" else "",
), unsafe_allow_html=True)


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

