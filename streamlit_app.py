import streamlit as st

st.set_page_config(page_title="ActivityFinder", layout="centered")

# CSS för att fixera navigationsfält i botten
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
    .bottom-nav a {
        text-decoration: none;
        color: #444;
        font-size: 18px;
    }
    .bottom-nav a.selected {
        color: #0066cc;
        font-weight: bold;
    }
    .block-container {
        padding-bottom: 80px;  /* space for nav */
    }
    </style>
""", unsafe_allow_html=True)


# 💡 Startsida
selected = st.experimental_get_query_params().get("page", ["home"])[0]

if selected == "🏠 Startsida":
    st.title("Välkommen till ActivityFinder 👋")
    st.markdown("""
    Här kommer du kunna:
    - Hitta aktiviteter i Göteborg
    - Filtrera efter datum, plats och kategori
    - Spara dina favoriter (kommer snart)

    Appen är anpassad för mobil – lägg till den på din hemskärm för snabb åtkomst!
    """)

# 🗺️ Karta – placeholder
elif selected == "🗺️ Karta":
    st.title("Karta")
    st.info("Denna funktion är inte aktiv ännu. Kommer snart!")

# ℹ️ Om
elif selected == "ℹ️ Om":
    st.title("Om appen")
    st.markdown("""
    Denna app är utvecklad för att göra det enkelt att upptäcka och planera evenemang i Göteborg.

    🛠️ Utvecklad med: [Streamlit](https://streamlit.io)  
    📱 Designad för: mobilanvändning  
    """)

# Navigeringsfält längst ner
st.markdown(f"""
    <div class="bottom-nav">
        <a href="/?page=home" class="{ 'selected' if selected == 'home' else '' }">🏠</a>
        <a href="/?page=map" class="{ 'selected' if selected == 'map' else '' }">🗺️</a>
        <a href="/?page=info" class="{ 'selected' if selected == 'info' else '' }">ℹ️</a>
    </div>
""", unsafe_allow_html=True)
