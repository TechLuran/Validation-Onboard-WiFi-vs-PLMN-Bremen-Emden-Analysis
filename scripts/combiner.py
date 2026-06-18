import os
import pandas as pd

# Ordnerpfade definieren
clean_folder = 'data/clean'
output_folder = 'data/clean'  # Kann angepasst werden, falls es woanders hin soll

# Die drei spezifischen Dateinamen auflisten
files_to_merge = [
    '11-13-leer-augustfeen.csv',
    '11-13-augustfeen-oldenburg.csv',
    '11-13-oldenburg-bremen.csv'
]

# Vollständige Pfade erstellen
file_paths = [os.path.join(clean_folder, f) for f in files_to_merge]

dataframes = []

for path in file_paths:
    if os.path.exists(path):
        print(f"Lese Datei ein: {path}")
        df = pd.read_csv(path)
        dataframes.append(df)
    else:
        print(f"Warnung: Datei wurde nicht gefunden: {path}")

if not dataframes:
    print("Fehler: Keine der angegebenen Dateien konnte gefunden werden.")
else:
    print("\nVerbinde Dateien...")
    # pd.concat fügt die Tabellen untereinander zusammen. 
    # Wenn eine Datei mehr Spalten hat, füllt Pandas die fehlenden Felder bei den anderen automatisch mit NaN auf.
    merged_df = pd.concat(dataframes, axis=0, ignore_index=True)
    
    # Zielpfad für die kombinierte Datei
    output_path = os.path.join(output_folder, '11-13-leer-bremen_combined.csv')
    
    # Speichern
    merged_df.to_csv(output_path, index=False)
    print(f"Erfolgreich zusammengeführt! Datei gespeichert unter: {output_path}")
    
    # Kurze Vorschau der Spalten im Terminal anzeigen
    print("\nVerfügbare Spalten in der neuen Datei:")
    print(list(merged_df.columns))