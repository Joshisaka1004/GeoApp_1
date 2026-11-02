# Karten 216, 218, 221–225 – Prüfmappe

Diese 7 Karten sind seit 2026-11-02 als DS78–DS84 in der App „Knobelwerk“. Die Karten 215, 217, 219 und 220 gibt es im Kartenordner nicht. Für 221–225 wurde die lektorierte Fassung vom 23.10. verwendet.

## Inhalt
- `Karten/`: Originalkarten DE und EN (unverändert)
- `App_Bilder/`: Zeichnungsausschnitte in der App, DE (`DSnn.png`) und EN (`DSnn_EN.png`)
- `Loesungen_*.md`: Original-Lösungen
- `App_Texte_DS78-84.swift`: Texte, Antworten, Hinweise und Lösungswege in der App (DE und EN)

## Zuordnung und Antworten in der App

| Karte | App | Titel | Antwort in der App | Thema |
|---|---|---|---|---|
| 216 | DS78 | Zickzack zwischen zwei Kreisen | 90° | Kreise |
| 218 | DS79 | Die Melone im Doppeltrog | 66,67 % (Toleranz 0,5) | Physik im Alltag |
| 221 | DS80 | Einmal rund um die Platte | 9 m² | Formen und Flächen |
| 222 | DS81 | Der Blick am Beet vorbei | 60° | Kreise |
| 223 | DS82 | Platten rund um die Säule | 144 Platten | Formen und Flächen |
| 224 | DS83 | Der Steg zwischen den Teichen | 82,76 % (Toleranz 0,3) | Kreise |
| 225 | DS84 | Der Stein kommt heim | 38,64 m (Toleranz 0,05) | Formen und Flächen |

Die App fragt nur nach einer Zahl. Deshalb wurden zwei Fragen angepasst:
- **218:** Der Bruchteil 2/3 wird in Prozent eingegeben.
- **224:** Gefragt ist nur Teil b), als Prozentzahl (24/29). Teil a), der Mittelpunktsabstand 10 m, steht im Lösungsweg.

## Befunde der ersten Prüfung (Claude)
- In den Zeichnungen wurden keine Mängel gefunden. Die Karten sind unverändert.
- Mit Python nachgerechnet:
  - **216:** zufällige Startpunkte ergeben jedes Mal 90°.
  - **222:** Minimum über die ganze Runde ist 60,0°.
  - **224:** verschiedene Radienpaare ergeben stets Abstand 10 und Anteil 24/29.
  - **225:** Startpunkt 38,637 m von A entfernt; die Probe landet in A.
  - **223:** die Flächenbilanz ergibt 96 Dreiecke und 48 Quadrate.
- Nicht unabhängig geprüft:
  - **218:** nur die Rechnung der Lösung nachvollzogen.
  - **221:** nur die Parkett-Zählung der Lösung nachvollzogen.

## Bitte besonders prüfen
1. **218:** Stimmen 2/3 und das Argument „Melone wirkt wie nachgefülltes Wasser“? Hängt etwas von der Höhe der Außenwände ab?
2. **221:** Gilt 12 · Fläche wirklich für jede Dreiecksform?
3. Allgemein:
   - Sind Text und Zeichnung eindeutig?
   - Fehlen Angaben, von denen die Lösung abhängt?
   - Stimmen die App-Texte mit den Karten überein?
