import requests
import pandas as pd
from requests.auth import HTTPBasicAuth

# API-url
url = "https://esb.goteborg.se/TEIK/Kalendarium/v1_0/activities?start=2025-06-01&end=2025-06-30"
username = "kalendarieapi"
password = r"V5S\eWs@"  # raw string för att undvika escape-problem

# API-anrop med Basic Auth
response = requests.get(url, auth=HTTPBasicAuth(username, password))

if response.status_code == 200:
    print("✅ Data hämtad")
    data = response.json()

    # Omvandla JSON till DataFrame
    df = pd.json_normalize(data)

    # Spara som CSV
    df.to_csv("kalendarium.csv", index=False, encoding='utf-8-sig')
    print("📁 Fil sparad som 'kalendarium.csv' – öppna i Excel!")

else:
    print("❌ API-anrop misslyckades:", response.status_code)
    print(response.text)

