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

elif menu == "🗺️ Karta":
    st.title("🗺️ Karta över aktiviteter")
    df = pd.read_csv("kalendarium_filtered.csv")
    df = df.dropna(subset=["latitude", "longitude"])
    df["latitude"] = pd.to_numeric(df["latitude"], errors="coerce")
    df["longitude"] = pd.to_numeric(df["longitude"], errors="coerce")
    st.map(df.rename(columns={"latitude": "lat", "longitude": "lon"}))

elif menu == "ℹ️ Om":
    st.title("ℹ️ Om appen")
    st.markdown("""
    Denna app är utvecklad för att göra det enkelt att upptäcka och planera evenemang i Göteborg.

    🛠️ Utvecklad med: [Streamlit](https://streamlit.io)  
    📱 Designad för: mobilanvändning  
    """)