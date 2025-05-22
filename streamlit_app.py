import streamlit as st
import pandas as pd
import numpy as np

# Sidomeny
menu = st.sidebar.radio(
    "Navigering",
    ["🏠 Startsida", "🏆 Poäng", "🗺️ Karta", "ℹ️ Om"]
)

if menu == "🏠 Startsida":
    st.title("Välkommen till ActivityFinder 👋")
    st.markdown("""
    Här kommer du kunna:
    - Hitta aktiviteter i Göteborg  
    - Filtrera efter datum, plats och kategori  
    - Spara dina favoriter (kommer snart)
    """)
    
     # Välj datumintervall
    st.subheader ("Hitta pågående evenemang:")
    start_date = st.date_input("Startdatum", value=None, key="start")
    end_date = st.date_input("Slutdatum", value=None, key="end")
    data = None
    
    df = pd.read_csv("kalendarium_filtered.csv")
    st.dataframe(df, use_container_width=True)

elif menu == "🏆 Poäng":
    st.title("🏆 Poäng")
    st.markdown ("""
    Här kommer du kunna se din poäng och din rank inom kort!")

elif menu == "🗺️ Karta":
    st.title("🗺️ Karta")
  

elif menu == "ℹ️ Om":
    st.title("ℹ️ Om appen")
    st.markdown("""
    Denna app är utvecklad för att göra det enkelt för familjer att upptäcka och planera aktiviteter i Göteborg, samt visa tillgängligheten.

    🛠️ Utvecklad med: [Streamlit](https://streamlit.io)  
    📱 Designad för: mobilanvändning  
    """)