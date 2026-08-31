import cdsapi
import zipfile
import csv
from pathlib import Path
from datetime import date, timedelta

LATITUDE = 45.9200365
LONGITUDE = 1.3704809

FICHIER_RECU = Path("copernicus_download.zip")

def telecharger_donnees(date):
    client = cdsapi.Client()

    dataset = "reanalysis-era5-land-timeseries"

    request = {
        "variable": ["volumetric_soil_water_level_1"],
        "location": {
            "longitude": LONGITUDE,
            "latitude": LATITUDE
        },
        "date": [date],
        "data_format": "csv"
    }

    client.retrieve(dataset, request).download(FICHIER_RECU)

def extraire_csv():
    with zipfile.ZipFile(FICHIER_RECU, "r") as archive:
        fichiers = archive.namelist()

        for fichier in fichiers:
            if fichier.endswith(".csv"):
                archive.extract(fichier)
                return Path(fichier)

    raise FileNotFoundError("Aucun fichier CSV trouvé dans l'archive Copernicus.")

def lire_humidite_sol(fichier_csv):
    donnees = []

    with open(fichier_csv, newline="", encoding="utf-8") as fichier:
        lecteur = csv.DictReader(fichier)

        for ligne in lecteur:
            donnees.append({
                "date": ligne["valid_time"],
                "humidite_m3_m3": float(ligne["swvl1"]),
                "latitude": float(ligne["latitude"]),
                "longitude": float(ligne["longitude"])
            })

    return donnees


def moyenne_journaliere(donnees):
    if not donnees:
        raise ValueError("Aucune donnée Copernicus disponible.")

    total = 0

    for ligne in donnees:
        total = total + ligne["humidite_m3_m3"]

    moyenne = total / len(donnees)

    return moyenne

def trouver_derniere_date_disponible():
    for decalage in range(5, 16):
        date_test = (date.today() - timedelta(days=decalage)).isoformat()

        try:
            telecharger_donnees(date_test)
            return date_test
        except Exception:
            continue

    raise RuntimeError("Aucune donnée Copernicus disponible sur les 15 derniers jours.")

if __name__ == "__main__":
    date_disponible = trouver_derniere_date_disponible()

    fichier_csv = extraire_csv()
    donnees = lire_humidite_sol(fichier_csv)
    moyenne = moyenne_journaliere(donnees)

    humidite_pourcent = moyenne * 100

    print(f"Humidité moyenne du sol — {date_disponible} : {humidite_pourcent:.2f} %")
    print("ERA5-Land · couche 0–7 cm")
