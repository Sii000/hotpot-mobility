import requests
import pandas as pd
from requests.auth import HTTPBasicAuth

# 1. API-anrop
url = "https://esb.goteborg.se/TEIK/Kalendarium/v1_0/activities?start=2025-06-01&end=2025-06-30"
username = "kalendarieapi"
password = r"V5S\eWs@"  # raw string pga \

response = requests.get(url, auth=HTTPBasicAuth(username, password))

if response.status_code == 200:
    print("✅ Data hämtad")
    data = response.json()

    # 2. Omvandla till DataFrame
    df = pd.json_normalize(data)  # plattar ut nested JSON

    # 3. Spara till CSV
    df.to_csv("kalendarium.csv", index=False, encoding='utf-8-sig')
    print("📁 CSV sparad som 'kalendarium.csv'")

else:
    print("❌ Fel vid anrop:", response.status_code)
    print(response.text)
