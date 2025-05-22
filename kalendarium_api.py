import requests
import pandas as pd
from requests.auth import HTTPBasicAuth

# API-info
url = "https://esb.goteborg.se/TEIK/Kalendarium/v1_0/activities?start=2025-06-01&end=2025-06-30"
username = "kalendarieapi"
password = r"V5S\eWs@"

# Hämta data
response = requests.get(url, auth=HTTPBasicAuth(username, password))

if response.status_code == 200:
    print("✅ Data hämtad")
    raw_data = response.json()
    activities = raw_data.get("content", [])

    # Normalisera nested JSON
    df = pd.json_normalize(activities)

    # 🎯 Välj bara dessa kolumner (lägg till fler om du vill!)
    desired_columns = [
        "title",
        "description",
        "startTime",
        "endTime",
        "location.name",
        "location.address",
        "location.city",
        "audience",
        "tags"
    ]

    # Filtrera kolumner som faktiskt finns
    available_columns = [col for col in desired_columns if col in df.columns]
    df_filtered = df[available_columns]

    # Spara som CSV
    df_filtered.to_csv("kalendarium_filtered.csv", index=False, encoding="utf-8-sig")
    print("📁 Filen 'kalendarium_filtered.csv' är klar – öppna i Excel!")

else:
    print("❌ Fel vid API-anrop:", response.status_code)
    print(response.text)
