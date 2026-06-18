import os
from glob import glob
import pandas as pd

# Ordnerpfade definieren
input_folder = 'data/raw/wifi-pings-(old-times-utc)'
output_folder = 'data/clean'

# Falls der Zielordner noch nicht existiert, wird er automatisch erstellt
os.makedirs(output_folder, exist_ok=True)

# Alle CSV-Dateien aus dem Quellordner zusammensuchen
csv_files = glob(os.path.join(input_folder, '*.csv'))

if not csv_files:
    print(f"Keine CSV-Dateien im Ordner '{input_folder}' gefunden.")
else:
    print(f"{len(csv_files)} Datei(en) gefunden. Starte Konvertierung...")

    for file_path in csv_files:
        # Dateinamen ohne Ordnerpfad extrahieren
        file_name = os.path.basename(file_path)
        
        # Daten einlesen
        df = pd.read_csv(file_path)
        
        # NUR die normale 'timestamp'-Spalte verschieben (+2 Stunden)
        df['timestamp'] = pd.to_datetime(df['timestamp']) + pd.Timedelta(hours=2)
        
        # Exakt im alten Format mit 3 Nachkommastellen abspeichern
        df['timestamp'] = df['timestamp'].dt.strftime('%Y-%m-%d %H:%M:%S.%f').str[:-3]
        
        # Neuen Zielpfad in data/clean definieren
        output_path = os.path.join(output_folder, file_name)
        
        # Speichern (timestamp_ns bleibt absolut unverändert)
        df.to_csv(output_path, index=False)
        print(f" -> Verarbeitet und gespeichert: {output_path}")

    print("\nAlle Dateien erfolgreich angepasst!")