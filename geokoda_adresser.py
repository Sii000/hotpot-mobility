import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

# 1. Läs in CSV-filen
df = pd.read_csv("kalendarium_filtered.csv")

# 2. Skapa fullständig adress: platsnamn + "Göteborg"
df["full_address"] = df["location.name"].fillna("") + ", Göteborg"

# 3. Geokodare med begränsning
geolocator = Nominatim(user_agent="activityfinder")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

# 4. Geokoda
print("📍 Startar geokodning...")
df["location"] = df["full_address"].apply(geocode)
df["latitude"] = df["location"].apply(lambda loc: loc.latitude if loc else None)
df["longitude"] = df["location"].apply(lambda loc: loc.longitude if loc else None)

# 5. Spara resultat
df.drop(columns=["location"], inplace=True)
df.to_csv("kalendarium_geokodad.csv", index=False, encoding="utf-8-sig")

print("✅ Geokodning klar! Fil sparad som 'kalendarium_geokodad.csv'")
