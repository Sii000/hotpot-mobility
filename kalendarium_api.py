# kalendarium_api.py
import requests
from requests.auth import HTTPBasicAuth

# Grundfunktion för att hämta aktiviteter från Kalendarium-API:t
def fetch_kalendarium(start_date, end_date):
    url = f"https://esb.goteborg.se/TEIK/Kalendarium/v1_0/activities?start={start_date}&end={end_date}"
    username = "kalendarieapi"
    password = r"V5S\eWs@"  # råsträng så att \ tolkas korrekt

    try:
        response = requests.get(url, auth=HTTPBasicAuth(username, password))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("API-anropet misslyckades:", e)
        return None
