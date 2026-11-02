# Karten 208–214 – Prüfmappe

Diese 7 Karten sind seit 2026-11-02 als DS71–DS77 in der App „Knobelwerk“.

## Inhalt
- `Karten/`: Originalkarten DE und EN (unverändert)
- `App_Bilder/`: Zeichnungsausschnitte, wie sie die App zeigt
- `Loesungen_*.md`: Original-Lösungen zu den Karten
- `App_Texte_DS71-77.swift`: Texte, Antworten, Hinweise und Lösungswege in der App (DE und EN)

## Zuordnung und Antworten in der App

| Karte | App | Titel | Antwort in der App |
|---|---|---|---|
| 208 | DS71 | Die Bogenfliesen | 2400 cm² |
| 209 | DS72 | Hundert Punkte im Park | 3 (Station C, A = 1 … H = 8) |
| 210 | DS73 | Der Riesenball im Lampenlicht | 3,2 m (Rollweg) |
| 211 | DS74 | Die Segel am Ovalteich | 14 m² |
| 212 | DS75 | Der Rahmen ohne Schachtel | 56 Teile |
| 213 | DS76 | Der Sandtisch an der Mauer | 126 Liter |
| 214 | DS77 | Immer geradeaus | 160 cm |

Die App fragt nur nach einer Zahl. Deshalb wurden drei Fragen angepasst:
- **209:** Die Station wird als Nummer eingegeben.
- **210:** Gefragt ist nur der Rollweg. Die Schattenfläche 15π/4 ≈ 11,78 m² steht im Lösungsweg.
- **213:** Gefragt sind nur die Liter. Die Höhe 45 cm steht im Lösungsweg.

## Befunde der ersten Prüfung (Claude)
- In den Zeichnungen wurden keine Mängel gefunden. Die Karten sind unverändert.
- Die Ergebnisse wurden so nachgeprüft:
  - **211:** mit Koordinaten nachgerechnet.
  - **214:** simuliert (160 cm in 28 Stücken).
  - **209:** alle Schilder gegen die Stationswerte geprüft. Die Reste mod 13 sind verschieden.
  - **210, 212, 213:** von Hand nachgerechnet.
- **208:** Nur mit der Sehnen-Probe aus der Lösung selbst geprüft, nicht unabhängig nachgezählt.

## Bitte besonders prüfen
1. **208:** Ist die gelbe Fläche wirklich 2400 cm²? Bitte die Fliesen im Bild unabhängig nachzählen.
2. **210:** Brennpunkt-Ansatz, insbesondere TS = 5/4 · d und dass die Schattenbreite konstant 3 m bleibt.
3. **213:** Darf man das Sandvolumen per Spiegelung an der Mauer als halbes „Dach“ über dem Drachen (Inkreis ρ = 0,6 m) berechnen?
4. Allgemein:
   - Sind Text und Zeichnung eindeutig?
   - Fehlen Angaben, von denen die Lösung abhängt?
   - Stimmen die App-Lösungswege in `App_Texte_DS71-77.swift` mit den Karten überein?
