# Korrekturen nach dem Prüfbericht vom 02.11.2026

Die Originale in `GeoRaetsel_natural/` bleiben unverändert. Hier liegen nur die geänderten Dateien.

## GR 06 (Aufgabenbild DE/EN, Lösungstexte)
Die Unterschrift „beliebiges Viereck, beliebiger Punkt“ war zu allgemein. Neue Bedingung: Punkt auf der Unterseite, Rot liegt ganz im Blau, und vom Punkt aus gesehen liegt die Mitte der Diagonale nach links oben links von der anderen Diagonalenmitte.
Nachgeprüft mit 200 000 Zufallsvierecken: Mit dieser Bedingung gilt A = B + C + 3 · D immer. Nur „Rot im Blau“ reicht nicht; in rund 11 % dieser Fälle ist das rote Dreieck spiegelverkehrt orientiert, dann gilt großes Dreieck − beide grünen = −4 · Rot.
Die Unterschrift ist dafür dreizeilig; `Werkzeug_natural/georaetsel_natural.py` setzt mehrzeilige Unterschriften kleiner (einzeilige Karten unverändert).

## GR 08 (Lösungsbild DE/EN)
Die inneren Gleichheitspaare tragen jetzt eigene Zeichen: rote Kreuze für die beiden gleichen Stücke auf der Linie zur Mitte der Grundseite (je 3,30), blaue Doppelkreuze für die beiden gleichen Stücke auf der Linie von der rechten Ecke (je 4,33). Die Striche gelten nur noch für die Seitenteilungen.

## GR 16 (Lösungsbild DE/EN, Lösungsschritte 3–5)
Die Vierteldrehung allein deckt die freie weiße Fläche nicht. Vollständige Zerlegung: Rot um 90° um die Mitte des großen Quadrats drehen. Es deckt die freie Fläche (gelb) bis auf ein Dreieck oben rechts und ragt unten rechts mit einem Dreieck (schraffiert, genau der Teil des rechten kleinen Quadrats im großen) über. Dieses Dreieck um weitere 90° gedreht füllt die Lücke genau.
Nachgerechnet an den Zeichenkoordinaten: Gelb = Rot = 23,5446; das schraffierte Dreieck und die Lücke je 15,0686; gedrehtes Rot ohne Schraffur plus Lücke ergibt die gelbe Fläche bis auf 10⁻¹⁴.
In der App (Knobelwerk, DS70) sind Lösungsschritte 3–5 und der zweite Hinweis entsprechend neu geschrieben.
