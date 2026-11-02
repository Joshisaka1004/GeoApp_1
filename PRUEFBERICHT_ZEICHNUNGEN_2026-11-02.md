# Zeichnerische Prüfung von GeoApp_1

Prüfer: Codex. Geprüft am 02.11.2026. Repository: [Joshisaka1004/GeoApp_1](https://github.com/Joshisaka1004/GeoApp_1), Branch `main`, Commit `f073ad9b1022f62d7b4a06ade03c1e2bbfd0363f`.

## Einschätzung

Die Sammlung ist zeichnerisch überwiegend gut und als Grundlage für die App geeignet. Ich habe keinen großen Konstruktionsfehler in den 16 Grundfiguren gefunden. Winkel, rechte Winkel, Kreisberührungen, Seitenlagen und die geprüften Flächen passen zu den Zeichnungen. Drei mittlere Befunde sollten vor einer unveränderten Übernahme behoben werden: GR 06 braucht eine präzisere Bedingung; die Lösungsbilder von GR 08 und GR 16 sollten überarbeitet werden. Die jeweiligen Befunde betreffen beide Sprachen.

Die Aufgabenbilder von GR 08 und GR 16 sind davon nicht betroffen. Bei den übrigen 13 Aufgabenpaaren sehe ich keinen mittleren oder großen zeichnerischen Befund. Kleine stilistische Unterschiede, sehr kleine Rundungsabweichungen der Kreisapproximationen und gewöhnliche Schnittpunkte dichter Hilfslinien habe ich nicht beanstandet.

## Die drei Befunde

### 1. GR 08: Gleichheitsstriche behaupten falsche Längengleichheiten

**Gewichtung: mittel. Betroffen: Lösungsbilder DE und EN.**

[Deutsches Lösungsbild](https://github.com/Joshisaka1004/GeoApp_1/blob/f073ad9b1022f62d7b4a06ade03c1e2bbfd0363f/GeoRaetsel_natural/GR_08_Loesung_DE.png) · [Zeichencode](https://github.com/Joshisaka1004/GeoApp_1/blob/f073ad9b1022f62d7b4a06ade03c1e2bbfd0363f/GeoRaetsel_natural/skripte/GR_08.py#L33)

Das Aufgabenbild verwendet einen Strich für die beiden Hälften der Grundseite, zwei für die Drittel der rechten Seite und drei für die Viertel der linken Seite. Im Lösungsbild kommen neue Gleichheitspaare im Inneren hinzu, erneut mit einem beziehungsweise zwei Strichen. Damit werden unterschiedliche Längengruppen miteinander gleichgesetzt.

In den Zeichenkoordinaten sind die Grundseitenhälften jeweils **6**, die mit demselben Einzelstrich markierten inneren Strecken aber nur **3,29848** lang. Bei den Doppelstrichen stehen **3,77124** auf der rechten Außenseite **4,32666** im Inneren gegenüber. Das ist eine echte falsche geometrische Aussage, keine Frage des Geschmacks.

**Empfehlung:** Die beiden zusätzlich eingeführten Gleichheitspaare durch eindeutig andere Zeichen kennzeichnen. Das Aufgabenbild und das Ergebnis Rot : Blau = 1 : 1 stimmen; beide Flächen sind in den Zeichenkoordinaten 4,8.

### 2. GR 06: „Beliebiges Viereck, beliebiger Punkt“ ist zu allgemein

**Gewichtung: mittel. Betroffen: Bedingung der Aufgabenkarte und allgemeiner Anspruch der Lösung, DE und EN.**

[Aufgabenbild](https://github.com/Joshisaka1004/GeoApp_1/blob/f073ad9b1022f62d7b4a06ade03c1e2bbfd0363f/GeoRaetsel_natural/GR_06_DE.png) · [Zeichencode](https://github.com/Joshisaka1004/GeoApp_1/blob/f073ad9b1022f62d7b4a06ade03c1e2bbfd0363f/GeoRaetsel_natural/skripte/GR_06.py)

Die konkret gezeichnete Figur ist korrekt. Der untere Punkt liegt auf einer Seite, die beiden markierten Punkte sind Diagonalenmitten, und das rote Dreieck liegt vollständig im oberen Dreieck. Für diese Zeichnung ergeben sich **A = 32,25**, **B = 6**, **C = 12**, **D = 4,75**; also tatsächlich A = B + C + 3D.

Die Bildunterschrift sagt aber „beliebiges Viereck, beliebiger Punkt“ beziehungsweise „any quadrilateral, any point“. Diese Allgemeinheit ist für die dargestellten gewöhnlichen Farbflächen nicht richtig. Selbst bei einem konvexen Viereck und einem Punkt auf der unteren Seite kann das rote Dreieck in die seitlichen grünen Bereiche hineinragen. Dann ändert sich die im Bild vorausgesetzte Flächenlage, und die Gleichung gilt so nicht mehr. Die im Archiv erwähnte Identität mit vorzeichenbehafteten Flächen beseitigt diesen Unterschied nicht.

**Empfehlung:** Die Lage ausdrücklich festhalten: Punkt auf der unteren Seite und rote Fläche vollständig im oberen Dreieck, mit dem Viereck in der gezeigten Anordnung. Den Ausdruck „beliebiger Punkt“ entsprechend einschränken. Die vorhandene Grundzeichnung muss dafür nicht neu konstruiert werden.

Ein nachgerechnetes Gegenbeispiel zur uneingeschränkten Formulierung: K=(0,0), L=(10,0), M=(6,1), N=(4,1), P=(5,0), E und F als Diagonalenmitten. Bei derselben Farbüberlagerung wäre die sichtbare blaue Fläche 0,75, die sichtbare grüne Fläche zusammen 4,25 und Rot 1. Die behauptete Gleichung würde 0,75 = 7,25 verlangen.

### 3. GR 16: Die eingezeichnete Drehung reicht für die Bildlösung nicht aus

**Gewichtung: mittel. Betroffen: Lösungsbilder DE und EN.**

[Lösungsbild](https://github.com/Joshisaka1004/GeoApp_1/blob/f073ad9b1022f62d7b4a06ade03c1e2bbfd0363f/GeoRaetsel_natural/GR_16_Loesung_DE.png) · [Zeichencode](https://github.com/Joshisaka1004/GeoApp_1/blob/f073ad9b1022f62d7b4a06ade03c1e2bbfd0363f/GeoRaetsel_natural/skripte/GR_16.py#L59)

Die Aufgabenzeichnung mit den drei Quadraten stimmt. Auch das Ergebnis **Rot : Blau = 1 : 2** ist richtig: Die gezeichneten Flächen betragen ungefähr 23,54464 und 47,08928.

Die Lösung zeigt eine Vierteldrehung des roten Dreiecks um die Mitte des großen Quadrats. Das gestrichelte gedrehte Dreieck deckt die benötigte freie weiße Restfläche jedoch nicht ab. Ein erheblicher Teil liegt in Bereichen, die bereits zu den kleinen Quadraten gehören; dafür bleibt ein anderer Teil der Restfläche unbedeckt. Rund **64 % des gedrehten Dreiecks liegen außerhalb der benötigten Restfläche**; ebenso bleiben rund 64 % dieser Restfläche unbedeckt. Das ist kein winziger zeichnerischer Spalt.

Der ausführliche Lösungstext erwähnt noch ein zusätzliches Umlegen eines Stücks. Dieser Schritt wird im Lösungsbild nicht dargestellt. Auch die Formulierung „Weiß im großen“ wird durch die gleichbleibend weißen Überlappungsbereiche der Quadrate nicht eindeutig sichtbar erklärt.

**Empfehlung:** Die gemeinte Restfläche ausdrücklich kennzeichnen und die fehlende Zerlegung beziehungsweise Umlegung zeigen; gegebenenfalls zwei Lösungsschritte verwenden. Eine vollständige Deckung durch die gezeichnete Vierteldrehung allein sollte die Karte nicht nahelegen.

**Nachrechenbare Gegenprobe:** Sei Q das große Quadrat, S die Vereinigung der beiden kleinen Quadrate, R das rote Dreieck und R′ das im Lösungsbild um 90° um die Quadratmitte gedrehte Dreieck. Die hier gemeinte freie weiße Restfläche ist W = Q ∖ (S ∪ R). Dann gilt in den vorhandenen Zeichenkoordinaten:

| Fläche | Inhalt |
|---|---:|
| R | 23,5446385380 |
| Blau | 47,0892770761 |
| W | 23,5446385380 |
| R′ außerhalb von W | 15,0685686643 |
| W außerhalb von R′ | 15,0685686643 |

Die Flächengleichheit von R und W stimmt. Eine unmittelbare Deckung durch die eingezeichnete Drehung stimmt dagegen nicht.

## Einzelübersicht

| Aufgabe | Zeichnerisches Urteil | Wesentliche Prüfung |
|---|---|---|
| GR 01 – drei Quadrate | Geeignet | Quadratlagen, Mittelpunktmarkierung und blaue Stücke stimmen; Blau = 73. |
| GR 02 – Winkel 2x/3x/4x | Geeignet | Winkel stehen an den richtigen Scheiteln und in den richtigen Sektoren. Tatsächliche Winkel 12°, 18°, 24°; ergänzte 30° und Lote stimmen. |
| GR 03 – Achtel- und Halbkreise | Geeignet | Die vier Stücke liegen im Außenkreis und überlappen sich nicht flächig. Die obere rechte Ecke des großen Achtelkreises liegt tatsächlich auf dem Außenkreis. Anteil 1/2 bestätigt. |
| GR 04 – Achteck | Geeignet | Regelmäßiges Achteck, markierte Seitenmitten und Speichen passen. Innenfläche 1/3, acht Randdreiecke jeweils 1/12; die Lösung zerlegt die Gesamtfläche vollständig. |
| GR 05 – berührende Kreise | Geeignet | Beide Kreisberührungen und die gemeinsame Grundtangente stimmen. Die Strecken 20 und 15 gehen durch den Berührpunkt und stehen senkrecht; x = 12. |
| GR 06 – Flächenwaage im Viereck | Bedingung präzisieren | Konkrete Zeichnung und Gleichung stimmen. Die uneingeschränkte Formulierung beschreibt einen zu großen Figurenbereich; siehe Befund 2. |
| GR 07 – gleichseitiges Dach | Geeignet | Gleichheitsgruppen stimmen; Dach und ergänztes unteres Dreieck sind tatsächlich gleichseitig. 78°, 42° und x = 18° liegen richtig. |
| GR 08 – Halb/Drittel/Viertel | Aufgabe geeignet; Lösung überarbeiten | Seitenaufteilung und gefärbte Flächen stimmen. Zusätzliche Gleichheitsstriche der Lösung sind falsch gruppiert; siehe Befund 1. |
| GR 09 – zwei Dächer im Trapez | Geeignet | Beide rechten Winkel und damit die parallelen Grundseiten sind klar. Die Zahlen 18, 8, 27, 9 sitzen in den gemeinten Teilflächen; Grün = 25 stimmt. |
| GR 10 – Kreis im Quadrat | Geeignet | Kreis durch die linke untere Ecke und Berührung rechts stimmen. Die Maße 1 und 3 gehören zu den richtigen Reststrecken. Die grüne Gesamtfläche einschließlich der äußeren Kappen beträgt 33. |
| GR 11 – Rechteck und Seitenmitte | Geeignet | Rechteck, Halbierungsstriche, rechter Winkel und Winkelbeschriftungen stimmen. Die Ergänzung erzeugt die markierten gleichen Strecken und die 32°-Winkel; x = 58°. |
| GR 12 – Giebel über drei Quadraten | Geeignet | Alle drei Quadrate und die beiden Dachstrecken sind geometrisch konsistent. Dachlängen 22 und 19, rote Seite 13; die Hilfsmaße a und b passen zu den Projektionen. |
| GR 13 – Pagode | Geeignet | Viertelteilung der Grundseite, Quadratturm und seitliche Quadratketten passen zusammen. Die endliche Zeichnung stellt den ausdrücklich genannten unendlichen Prozess ausreichend dar; Anteil nähert sich 5/6. |
| GR 14 – Zelt | Geeignet für die gezeigte Lage | 2x = 50°, 4x = 100°, Außenwinkel 6x = 150° stimmen. Die Zeltstange kreuzt tatsächlich die Dreiecksseite; diese Seitenlage ist beim Neuzeichnen beizubehalten. Der ergänzte Kreis und das gleichseitige Dreieck sind korrekt. |
| GR 15 – Quadrat im Quadratrahmen | Geeignet | Beide Quadrate und die zugehörigen Rahmenflächen sind klar. Außenkante 10, gegenüberliegende Flächen 13 und 23, Innenfläche 28 stimmen. |
| GR 16 – drei einbeschriebene Quadrate | Aufgabe geeignet; Lösung ergänzen | Quadrate, Höhe, rechte Winkel und Verhältnis 1 : 2 stimmen. Die Bildlösung lässt eine wesentliche Flächenumlegung aus; siehe Befund 3. |

## Darstellung in einer App

Die Karten haben alle 1100 × 1100 Pixel und lassen sich als Ausgangsmaterial verwenden. Für eine Anzeige in voller Kartenbreite auf einem schmalen Smartphone sollte eine Vergrößerung möglich sein. Einzelne kleine Winkelangaben, Gleichheitsstriche und Bruchbeschriftungen werden sonst schwer lesbar, besonders in GR 08, GR 13 und GR 14. Das ist eine Frage der vorgesehenen Anzeigegröße; die vorliegenden Originalbilder sind nicht abgeschnitten.

## Umfang und Nachweise

- Alle 64 vorhandenen PNGs wurden in Kontaktbögen betrachtet: 16 Aufgaben und 16 Lösungen, jeweils DE und EN. Kritische Details wurden zusätzlich in Originalgröße betrachtet.
- Die Zeichenskripte aller 16 Aufgaben wurden gelesen. Die Zeichenfunktionen wurden ohne Überschreiben der Originale instrumentiert: sämtliche Winkelangaben, rechten Winkel und Gleichheitsgruppen wurden anhand ihrer Koordinaten kontrolliert. Außer den beschriebenen Gruppen von GR 08 wurden keine falschen Gleichheitsmarkierungen gefunden.
- Die erzeugten Textbegrenzungen wurden für alle 64 Kartendefinitionen kontrolliert; keine lag außerhalb der Bildfläche. In den Originalen wurde kein mittlerer oder großer Beschriftungszusammenstoß festgestellt.
- Berührungen, Flächenzerlegungen und wesentliche Längen wurden zusätzlich an den tatsächlichen Polygonen und Koordinaten nachgerechnet. Diese Kontrolle prüft die gezeichnete Geometrie; sie ist keine vollständige unabhängige Beweis- und Eindeutigkeitsprüfung sämtlicher allgemeiner Rätselsätze.
- Die 87 für die Prüfung heruntergeladenen Quelldateien wurden lokal anhand ihrer Git-Blob-Prüfsummen verifiziert; alle stimmen mit dem angegebenen GitHub-Stand überein. Dieser veröffentlichte Markdown-Bericht enthält die wesentlichen Messwerte, Gegenbeispiele und Quellverweise, sodass die Befunde ohne Zugriff auf den lokalen Projektordner nachgeprüft werden können.

Die Prüfung bezieht sich auf den oben genannten Commit. Auf Wunsch des Repository-Inhabers wurde dieser Prüfbericht anschließend als Markdown-Datei im Repository ergänzt. Aufgabenbilder, Lösungsbilder und Zeichenskripte wurden dabei nicht geändert; es wurde nichts in eine App eingebaut.
