import streamlit as st

st.set_page_config(page_title="Göteborgsappen", layout="centered")

# ⬅️ Menyval (vänstersida)
menu = st.sidebar.radio(
    "Navigera",
    ("🏠 Startsida", "🗺️ Karta", "ℹ️ Om")
)

# 💡 Startsida
if menu == "🏠 Startsida":
    st.title("Välkommen till ActivityFinder 👋")
    st.markdown("""
    Här kommer du kunna:
    - Hitta aktiviteter i Göteborg
    - Filtrera efter datum, plats och kategori
    - Spara dina favoriter (kommer snart)

    Appen är anpassad för mobil – lägg till den på din hemskärm för snabb åtkomst!
    """)

# 🗺️ Karta – placeholder
elif menu == "🗺️ Karta":
    st.title("Karta")
    st.info("Denna funktion är inte aktiv ännu. Kommer snart!")

# ℹ️ Om
elif menu == "ℹ️ Om":
    st.title("Om appen")
    st.markdown("""
    Denna app är utvecklad för att göra det enkelt att upptäcka och planera evenemang i Göteborg.

    🛠️ Utvecklad med: [Streamlit](https://streamlit.io)  
    📱 Designad för: mobilanvändning  
    """)

