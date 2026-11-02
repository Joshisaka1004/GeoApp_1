# Nachprüfung der Korrekturen GR 06, GR 08 und GR 16

Prüfer: Codex. Geprüft am 02.11.2026. Geprüfter Commit: [`b421db7527083cf8cfd7b486a3e30fab174696a7`](https://github.com/Joshisaka1004/GeoApp_1/commit/b421db7527083cf8cfd7b486a3e30fab174696a7).

## Ergebnis

**Alle drei mittleren Befunde des ersten Prüfberichts sind in den korrigierten Fassungen behoben.** Ich sehe in den sechs geänderten Bildern auf Deutsch und Englisch keinen verbleibenden mittleren oder großen zeichnerischen Befund. Zusammen mit den zuvor geprüften unveränderten Karten halte ich die Sammlung aus zeichnerischer Sicht für eine Verwendung in der App geeignet. Die bereits empfohlene Vergrößerungsmöglichkeit für kleine Bildschirme bleibt sinnvoll.

Die korrigierten Dateien liegen im Ordner [`GeoRaetsel_natural_korrigiert/`](https://github.com/Joshisaka1004/GeoApp_1/tree/b421db7527083cf8cfd7b486a3e30fab174696a7/GeoRaetsel_natural_korrigiert). Der ursprüngliche Ordner `GeoRaetsel_natural/` enthält weiterhin die alten Fassungen. Für die betreffenden sechs Bilder und die ergänzten Lösungstexte ist daher die korrigierte Fassung maßgeblich.

| Ursprünglicher Befund | Status | Nachprüfung |
|---|---|---|
| GR 06: zu allgemeine Figurenbedingung | **Erledigt** | Punkt auf der Unterseite, Enthaltensein des roten Dreiecks und die erforderliche Orientierung der Diagonalenmitten sind jetzt angegeben. |
| GR 08: falsche Gleichheitsgruppen | **Erledigt** | Rote Einzelkreuze und blaue Doppelkreuze kennzeichnen die zusätzlichen inneren Gleichheitspaare eindeutig getrennt von den seitlichen Teilungsstrichen. |
| GR 16: unvollständige Flächenumlegung | **Erledigt** | Die Zielfläche ist gelb hervorgehoben. Überstehendes Stück und Lücke werden gezeigt; die zusätzliche Vierteldrehung füllt die Lücke tatsächlich. |

## GR 06 – Bedingung präzisiert

[Aufgabenbild DE](https://github.com/Joshisaka1004/GeoApp_1/blob/b421db7527083cf8cfd7b486a3e30fab174696a7/GeoRaetsel_natural_korrigiert/GR_06_DE.png) · [Aufgabenbild EN](https://github.com/Joshisaka1004/GeoApp_1/blob/b421db7527083cf8cfd7b486a3e30fab174696a7/GeoRaetsel_natural_korrigiert/GR_06_EN.png) · [Zeichencode](https://github.com/Joshisaka1004/GeoApp_1/blob/b421db7527083cf8cfd7b486a3e30fab174696a7/GeoRaetsel_natural_korrigiert/skripte/GR_06.py)

Die dreizeilige Unterschrift nennt nun die Punktlage, das Enthaltensein des roten Dreiecks im oberen Dreieck und die Reihenfolge seiner beiden oberen Ecken vom unteren Punkt aus gesehen. Damit wird insbesondere das Vorzeichen der Flächenidentität festgelegt.

Die zusätzliche Orientierungsbedingung ist erforderlich. Mein früherer Korrekturvorschlag, nur Punktlage und Enthaltensein zu nennen, war an dieser Stelle zu kurz. Die jetzige Fassung berücksichtigt diesen Punkt.

Für die gezeichnete Figur sind Enthaltensein und Orientierung erfüllt; die Formelabweichung ist rechnerisch null. Eine zusätzliche Probe mit 15.000 zufällig erzeugten Anordnungen ergab 5.019 gültige Vierecke, die die neuen Bedingungen erfüllen, und darin keinen Gegenfall. Das ist eine numerische Gegenprobe, kein Ersatz für einen allgemeinen Beweis.

Beide Sprachfassungen wurden in Originalgröße betrachtet. Die neue Unterschrift ist vollständig innerhalb der Karte und kollidiert nicht mit dem Formelrahmen oder der Figur. Auch die entsprechenden Bedingungen in den deutschen und englischen Lösungstexten wurden ergänzt.

## GR 08 – Gleichheitsmarkierungen getrennt

[Lösungsbild DE](https://github.com/Joshisaka1004/GeoApp_1/blob/b421db7527083cf8cfd7b486a3e30fab174696a7/GeoRaetsel_natural_korrigiert/GR_08_Loesung_DE.png) · [Lösungsbild EN](https://github.com/Joshisaka1004/GeoApp_1/blob/b421db7527083cf8cfd7b486a3e30fab174696a7/GeoRaetsel_natural_korrigiert/GR_08_Loesung_EN.png) · [Zeichencode](https://github.com/Joshisaka1004/GeoApp_1/blob/b421db7527083cf8cfd7b486a3e30fab174696a7/GeoRaetsel_natural_korrigiert/skripte/GR_08.py)

Die falsche Wiederverwendung der Teilungsstriche ist beseitigt. Die beiden roten Einzelkreuze stehen auf Strecken der Länge 3,2984845005; die beiden blauen Doppelkreuze auf Strecken der Länge 4,3266615306. Innerhalb jeder neuen Gruppe stimmen die Längen überein. Die Markierungen sind durch Form, Anzahl und Farbe von den schwarzen Strichen an den Außenseiten zu unterscheiden.

In den beiden Lösungsbildern sehe ich damit keine falsche behauptete Längengleichheit mehr. Figur, Flächenbeschriftungen und Ergebnis 1 : 1 bleiben korrekt.

## GR 16 – Zerlegung und zweite Drehung ergänzt

[Lösungsbild DE](https://github.com/Joshisaka1004/GeoApp_1/blob/b421db7527083cf8cfd7b486a3e30fab174696a7/GeoRaetsel_natural_korrigiert/GR_16_Loesung_DE.png) · [Lösungsbild EN](https://github.com/Joshisaka1004/GeoApp_1/blob/b421db7527083cf8cfd7b486a3e30fab174696a7/GeoRaetsel_natural_korrigiert/GR_16_Loesung_EN.png) · [Zeichencode](https://github.com/Joshisaka1004/GeoApp_1/blob/b421db7527083cf8cfd7b486a3e30fab174696a7/GeoRaetsel_natural_korrigiert/skripte/GR_16.py)

Die freie Restfläche ist jetzt eindeutig gelb markiert. Das zunächst überstehende Dreieck ist schraffiert und mit 2 bezeichnet; ein zweiter Pfeil zeigt seine Umlegung in die Lücke. Die Beschriftung beschreibt beide Schritte und die Beziehung Blau = Gelb + Rot.

Die neue geometrische Konstruktion wurde unabhängig an den Polygonen nachgerechnet. Mit den Bezeichnungen des Skripts und O = (D + F)/2 bildet eine weitere 90°-Drehung um dieselbe Quadratmitte das schraffierte Dreieck (E, X, Z) auf das Lückendreieck (F, X2, Y) ab. Es ist also nicht nur gleich groß, sondern passt nach dieser Drehung in die gezeichnete Lücke.

| Kontrolle in den Zeichenkoordinaten | Ergebnis |
|---|---:|
| Rote Fläche | 23,5446385380 |
| Gelbe Fläche | 23,5446385380 |
| Blaue Fläche | 47,0892770761 |
| Schraffiertes Stück | 15,0685686643 |
| Lücke | 15,0685686643 |
| Nicht übereinstimmende Fläche nach vollständiger Umlegung | ca. 2,1 × 10⁻¹⁴ |

Die letzte Abweichung ist numerisches Rundungsrauschen. Die gelbe Hervorhebung stimmt ebenfalls mit der tatsächlich freien Restfläche überein. Damit ist der vorher fehlende Flächenschritt jetzt zeichnerisch und rechnerisch geschlossen. Die deutschen und englischen Lösungsschritte 3–5 beschreiben die ergänzte Konstruktion passend.

## Umfang der Nachprüfung

- Die sechs korrigierten PNGs wurden in Originalgröße betrachtet, beide Sprachfassungen jeweils vollständig.
- Alle 13 neu hinzugefügten Dateien wurden gelesen beziehungsweise betrachtet und lokal über ihre Git-Blob-Prüfsummen gegen den angegebenen Commit verifiziert.
- Die drei korrigierten Zeichenskripte und der geänderte Kartenhelfer wurden mit dem ursprünglichen Stand verglichen. Die Textbegrenzungen der sechs korrigierten Kartendefinitionen liegen vollständig innerhalb von 1100 × 1100 Pixeln.
- Die übrigen Karten und ursprünglichen Skripte sind im Korrekturcommit unverändert; ihre vorherige Bewertung gilt weiter.
- Die in `KORREKTUREN.md` erwähnten Änderungen in Knobelwerk wurden hier nicht geprüft. Diese Nachprüfung betrifft die im Repository vorhandenen Bilder, Skripte und Lösungstexte.

Es wurden bei der Nachprüfung keine Aufgabenbilder, Lösungsbilder oder Zeichenskripte verändert. Dieser Nachprüfbericht dokumentiert den jetzt erledigten Status der ursprünglichen Befunde.
