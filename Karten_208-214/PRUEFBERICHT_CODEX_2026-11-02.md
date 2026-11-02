# Prüfbericht: Karten 208–214 / App DS71–DS77

Prüfer: Codex. Geprüft am 02.11.2026. Repository: [Joshisaka1004/GeoApp_1](https://github.com/Joshisaka1004/GeoApp_1). Geprüfter Commit: [6640487d93a098016d0bfb94ebc44ea76cfa3369](https://github.com/Joshisaka1004/GeoApp_1/commit/6640487d93a098016d0bfb94ebc44ea76cfa3369).

## Ergebnis

**Alle sieben Karten sind aus zeichnerischer Sicht für die App geeignet. Ich habe keinen mittleren oder großen geometrischen beziehungsweise zeichnerischen Fehler gefunden. Auch die sieben in der App hinterlegten Antworten stimmen.**

Geprüft wurden die 14 Originalkarten DE/EN, alle sieben App-Bildausschnitte, die beiden mitgelieferten Lösungstexte und die deutschen und englischen Angaben, Fragen, Antworten, Hinweise und Lösungsschritte in der Swift-Datei. Kleine stilistische Unterschiede wurden nicht beanstandet. Ein Hinweis zur Sprache der App-Bilder steht am Ende dieses Berichts.

| Karte | App | Urteil | Unabhängig bestätigtes Ergebnis |
|---|---|---|---|
| 208 – Die Bogenfliesen | DS71 | Geeignet | 2400 cm² |
| 209 – Hundert Punkte im Park | DS72 | Geeignet | Station C; App-Eingabe 3 |
| 210 – Der Riesenball im Lampenlicht | DS73 | Geeignet | Rollweg 3,2 m; Schattenfläche 15π/4 m² ≈ 11,78097 m² |
| 211 – Die Segel am Ovalteich | DS74 | Geeignet | 14 m² |
| 212 – Der Rahmen ohne Schachtel | DS75 | Geeignet | 56 Randteile einschließlich Ecken |
| 213 – Der Sandtisch an der Mauer | DS76 | Geeignet | 126 Liter; größte Höhe 45 cm |
| 214 – Immer geradeaus | DS77 | Geeignet | 160 cm in 28 Teilstücken |

## 208 – Fliesen im Bild unabhängig nachgezählt

[App-Bild DS71](https://github.com/Joshisaka1004/GeoApp_1/blob/6640487d93a098016d0bfb94ebc44ea76cfa3369/Karten_208-214/App_Bilder/DS71.png)

Die rote und die blaue Schlaufe sind geschlossen, schneiden sich nicht und begrenzen eindeutig die gelbe Fläche. Die blaue Kreisfläche ist ausgespart. Die Fliesenmaße 20 cm und der Bogenradius 10 cm passen zu den gezeichneten Halbseiten.

Ich habe den Verlauf der 20 roten Viertelkreisbögen aus dem Bild abgelesen und die gelben Stücke pro Fliese bestimmt. Das ist eine eigene Nachzählung am Bild, nicht nur eine Übernahme der Sehnen-Probe.

Zählung ab links oben im sichtbaren 6×6-Raster: S = gelbes S-Band, V = gelber Viertelkreis, – = kein gelbes Stück.

| Zeile von oben / Spalte von links | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| 1 | V | V | V | V | – | – |
| 2 | V | S | S | S | V | – |
| 3 | V | S | S | S | V | – |
| 4 | V | V | V | V | – | – |
| 5 | – | – | – | – | – | – |
| 6 | – | – | – | – | – | – |

Damit sind es **6 Bänder und 12 Viertelkreise**. Ein Viertelkreis hat 25π cm², ein Band 400 − 50π cm²:

**Gelb = 6 · (400 − 50π) + 12 · 25π = 2400 cm².**

Zusätzlich habe ich den beobachteten roten Bogenverlauf über das Kurvenintegral ½∮(x dy − y dx) berechnet. In Fliesenflächen ergibt das außen 6 + π/4 und innen π/4, also erneut genau 6 Fliesen. Die polygonale Näherung mit fein abgetasteten Bögen ergibt 2399,99988 cm²; die geringe Abweichung stammt aus der Näherung.

Die in der Lösung genannten Bandpositionen „Spalten 2 bis 4, Zeilen 4 und 5 von unten“ sind dieselben sechs Felder wie Zeilen 2 und 3 von oben. Zeichnung, Lösung und App-Text stimmen überein.

## 209 – Alle Pfeile und Zahlen kontrolliert

[App-Bild DS72](https://github.com/Joshisaka1004/GeoApp_1/blob/6640487d93a098016d0bfb94ebc44ea76cfa3369/Karten_208-214/App_Bilder/DS72.png)

Die Pfeile sind den jeweiligen Wegen eindeutig zugeordnet; an Kreuzungen gibt es keine unbezeichneten zusätzlichen Stationen. Die acht Stationen und der Startpunkt A sind klar markiert.

Alle 16 Pfeilrichtungen und Zahlen wurden aus dem Bild übertragen und nachgerechnet. Um jede der acht dreieckigen Rasenflächen ist die Punktesumme tatsächlich 0. Die Runde B→E→D→C→B bringt −6 + 23 + 14 − 18 = 13.

Die Stationsreste modulo 13 sind:

| Station | A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|---|
| Rest | 0 | 4 | 9 | 8 | 11 | 7 | 2 | 5 |

100 hat Rest 9, deshalb kommt nur C infrage. Eine eigene Suche im Zustandsgraphen bestätigt außerdem die angegebene kürzeste Route mit 22 Wegstücken. Die App-Umrechnung C → Nummer 3 ist korrekt.

## 210 – Schattenmodell unabhängig von der Brennpunkt-Lösung geprüft

[App-Bild DS73](https://github.com/Joshisaka1004/GeoApp_1/blob/6640487d93a098016d0bfb94ebc44ea76cfa3369/Karten_208-214/App_Bilder/DS73.png)

Die Zeichnung unterscheidet Startball, aktuellen Ball und Bodenschatten verständlich. Die 3 m und 5 m gehören zu den Schattenausdehnungen, der gesuchte Rollweg zum Standort des Balls. Die in der Kugel verdeckte Schattenkontur ist gestrichelt dargestellt. Die perspektivische Ansicht ist mit einem kreisförmigen Startschatten und einem elliptischen späteren Schatten vereinbar.

Zur unabhängigen Rechnung: Lampe L=(0,0,h), Kugelmittelpunkt I=(d,0,r), Boden z=0. Aus der Tangentenbedingung für den Strahl L→(x,y,0) folgt für den Schattenrand:

A x² + K y² − 2 d h (h−r) x + h²(d²−r²) = 0,

mit A=h(h−2r) und K=A+d². Daraus folgen die Ellipsenhalbachsen und das Zentrum:

- b² = h r² / (h−2r), also unabhängig vom Rollweg d;
- a² = b² · (1 + d²/A);
- x₀ = d(h−r)/(h−2r).

Mit r=1 m und dem anfänglichen Schattenradius 1,5 m erhält man **h=3,6 m**. Die halbe Schattenbreite bleibt **b=1,5 m**. Aus der späteren halben Länge a=2,5 m folgt **d=3,2 m**.

Das Schattenzentrum liegt dann bei x=5,2 m, die beiden Enden bei x=2,7 m und x=7,7 m. Beide zugehörigen Randstrahlen haben genau 1 m Abstand vom Kugelmittelpunkt: Sie sind tatsächlich Tangenten.

Die Brennpunkte liegen bei 3,2 m und 7,2 m. Damit ist TS=4 m=5d/4; auch dieser ausdrücklich zur Prüfung gestellte Zusammenhang stimmt. Der untere Dandelin-Kugelradius R=2,25 m und die konstante Schattenbreite 3 m sind korrekt.

Die Fläche ist πab=15π/4 m²≈11,78097 m². Die App fragt bewusst nur den Rollweg ab und führt die Fläche zusätzlich im Lösungsweg auf. Diese Anpassung ist konsistent.

## 211 – Pfostenlage, Segel und Flächen stimmen

[App-Bild DS74](https://github.com/Joshisaka1004/GeoApp_1/blob/6640487d93a098016d0bfb94ebc44ea76cfa3369/Karten_208-214/App_Bilder/DS74.png)

Die beiden Teilbilder zeigen dieselben vier Pfosten an denselben Uferpositionen und unterschiedliche Laternenplätze. Alle sechs Punkte liegen auf dem Oval. Die roten und blauen Dreiecke überlappen sichtbar; Text und Legende stellen jedoch ausdrücklich klar, dass jedes Segel einzeln gemessen wird. Daraus entsteht keine falsche Aussage über die Fläche einer Farbvereinigung.

Die passende Koordinatenfigur auf x²/100+y²/25=1 wurde mit Dreiecksdeterminanten nachgerechnet. Es ergeben sich:

| Laternenplatz | PAB | PCD | PAC | PBD |
|---|---:|---:|---:|---:|
| P1 | 64 | 6 | 12 | 48 |
| P2 | 28 | 8 | 24 | **14** |

Alle Werte in m². Der Quotient (PAB·PCD)/(PAC·PBD) ist beide Male 2/3. Die Rückführung des Ovals auf einen Kreis und die Kürzung der Flächenskalierung sind richtig.

## 212 – Puzzleteile und Rahmenzählung passen

[App-Bild DS75](https://github.com/Joshisaka1004/GeoApp_1/blob/6640487d93a098016d0bfb94ebc44ea76cfa3369/Karten_208-214/App_Bilder/DS75.png)

Nase, Loch und gerade Kante werden verständlich gezeigt. Die Schalen sind ausdrücklich nach Nasenzahl beschriftet; die sichtbaren Teile widersprechen ihrer Zuordnung nicht. Die gezeichneten Beispielstücke sind erkennbar keine zeichnerische Darstellung aller 17 beziehungsweise 59 Teile. Das Fragezeichen bei „2 Nasen“ ist durch „nicht gezählt“ ausreichend erklärt.

Die Rechnung über alle Teile ist korrekt: Jede innere Verbindung liefert genau eine Nase und ein Loch. Die Zahl der geraden Randkanten beträgt deshalb

4·17 + 2·59 − 2·49 − 4·7 = **60**.

Die unbekannte Zahl der Teile mit zwei Nasen trägt 0 bei. Wegen der vier Ecken sind es **60−4=56 Randteile**. Die Formulierung mit mehreren Reihen und Spalten schließt die Sonderfälle eines einreihigen oder einspaltigen Puzzles aus.

## 213 – Sandvolumen direkt integriert, Spiegelung bestätigt

[App-Bild DS76](https://github.com/Joshisaka1004/GeoApp_1/blob/6640487d93a098016d0bfb94ebc44ea76cfa3369/Karten_208-214/App_Bilder/DS76.png)

Die Draufsicht ist als solche bezeichnet. Die Mauer liegt an der 1,4-m-Seite; die freien Kanten sind 1,5 m und 1,3 m lang. Das 3:4-Steigungsdreieck ist getrennt von der Draufsicht angeordnet und eindeutig als steilste Sandoberfläche beschriftet. Die Seitenverhältnisse der gezeichneten Platte passen zu den Angaben.

Ich habe das Volumen direkt aus dem beschriebenen Höhenmodell geprüft, ohne die Spiegelung vorauszusetzen. In Dezimetern kann man A=(0,0), B=(14,0), C=(9,12) wählen. Für einen Punkt P gilt

h(P) = ¾ · min(Abstand zu AC, Abstand zu BC).

An der Mauer ist keine Nullhöhe vorgeschrieben. Die beiden Dachflächen treffen sich über der Winkelhalbierenden CD mit **D=(7,5;0)**. D hat zu beiden freien Kanten 6 dm Abstand. Also ist die größte Höhe **4,5 dm=45 cm**; die 2 m hohe Mauer ist dafür ausreichend hoch.

Die beiden Grunddreiecke ACD und BCD haben Flächen 45 dm² und 39 dm². Über jedem ist die Höhenfunktion eben und steigt von der freien Kante bis D linear an. Direkt integriert ergibt das

V = (45+39) · 4,5 / 3 = **126 dm³ = 126 Liter**.

Damit ist auch die Spiegelungsrechnung bestätigt: Der hier entstehende konvexe Drachen hat Fläche 168 dm² und einen tatsächlichen Inkreis mit Radius 6 dm; der Haufen ist die Hälfte der entsprechenden Pyramide. Die App lässt bewusst nur die Literzahl eingeben und erklärt die Höhe im Lösungsweg. Das passt.

## 214 – Würfelweg exakt in 3D simuliert

[App-Bild DS77](https://github.com/Joshisaka1004/GeoApp_1/blob/6640487d93a098016d0bfb94ebc44ea76cfa3369/Karten_208-214/App_Bilder/DS77.png)

Anfang in der unteren Kantenmitte und Auftreffhöhe 3 cm an der rechten Vorderkante sind eindeutig. Die zusätzliche Vorderansicht macht die Richtung 4:3 unabhängig von der räumlichen Perspektive klar. Auch die gezeichnete Fortsetzung auf der rechten Seitenfläche ist mit dem knickfreien Verlauf auf dem abgewickelten Würfel vereinbar. Eine perspektivisch veränderte Steigung auf dem Papier ist dabei richtig.

Eine eigene Simulation mit exakten Brüchen verfolgt auf dem Würfel [0,8]³ den Anfang (4,0,0), zunächst auf y=0 mit Tangentenvektor (4,0,3). An jeder erreichten Kante wird der Tangentenvektor um 90° in die angrenzende Fläche gedreht.

Ergebnis: **160 cm, 28 Teilstücke, kein Würfeleckendurchgang.** Der Anfang wird vorher auch nicht mit einer anderen Laufrichtung besucht.

Die ersten sieben Teilstücke liegen auf Vorderseite, rechter Seite, Oberseite, Hinterseite, Unterseite, linker Seite und wieder Vorderseite. Ihre Längen sind 5, 25/3, 5/3, 10, 5/3, 25/3 und 5 cm, zusammen 40 cm. Nach 40, 80 und 120 cm liegen die entsprechenden Mittelpunkte jeweils an anderen Kanten; nach 160 cm stimmen Anfangspunkt und Richtung wieder überein. Die Vierteldrehungsargumentation im Lösungstext ist korrekt.

## App-Ausschnitte, Sprache und angepasste Fragen

Die sieben App-Bilder erhalten die für die Aufgaben nötigen geometrischen Angaben, Maßzahlen und Legenden. Beim Vergleich mit den Originalkarten liegt die innere Bildfläche jeweils unverändert bei einem Versatz von (50,497) Pixeln; die Unterschiede am Außenrand betreffen die aufgefüllten abgerundeten Ecken. Es ging dadurch keine wichtige Angabe verloren.

Die in der README dokumentierten Anpassungen sind richtig umgesetzt:

- 209: C wird als Stationsnummer 3 eingegeben.
- 210: Nur der Rollweg ist die Eingabe; die zusätzliche Schattenfläche steht weiterhin in der Lösung.
- 213: Nur die Literzahl ist die Eingabe; die größte Höhe wird weiterhin erklärt.

**Hinweis für eine englische App-Ausgabe:** Die vollständigen englischen Originalkarten sind passend übersetzt. Im gelieferten Ordner App_Bilder liegen jedoch nur die sieben deutschen Ausschnitte, beispielsweise mit „Nasen“, „Mauer“, „rote Schlaufe“ und „Vorderseite“. Wenn die App diese Dateien auch in ihrer englischen Ansicht verwendet, sollten dort entsprechende Ausschnitte aus den englischen Originalkarten verwendet werden. Die tatsächliche sprachabhängige Bildauswahl der laufenden App ist in dieser Prüfmappe nicht enthalten; deshalb ist das ein Integrationshinweis und kein nachgewiesener Fehler der laufenden App.

## Prüfumfang und Grenzen

- Alle 21 PNGs wurden betrachtet: 14 Karten in DE/EN und sieben App-Zeichnungen. Geometrische Details wurden anhand der App-Bilder in voller Originalgröße geprüft; kritische Originalkarten wurden zusätzlich vergrößert betrachtet.
- Beide Lösungstexte, die README und die Swift-Datei mit den zweisprachigen App-Texten wurden gelesen und mit den Bildern und Antworten verglichen.
- Die sieben Antworten wurden unabhängig nachgerechnet; der Fliesenverlauf und alle 16 Parkpfeile wurden dafür aus den Bildern neu übertragen.
- Die 25 heruntergeladenen Quelldateien wurden anhand ihrer Git-Blob-Prüfsummen gegen den angegebenen Commit verifiziert.
- Für diese Serie liegen keine Zeichenskripte und keine separaten Lösungsbild-PNGs in der Prüfmappe vor. Die Prüfung bezieht sich auf die fertigen Bilder, ihre geometrische Konsistenz und die mitgelieferten Lösungstexte.
- Dies ist keine Laufzeitprüfung oder Bildschirmgrößenprüfung der App. Die Bilder und Textdaten der App wurden so geprüft, wie sie im Repository bereitgestellt sind.

**Keine Korrektur an den sieben geometrischen Aufgaben oder ihren Ergebnissen erforderlich.** Dieser Bericht wurde auf Wunsch im Repository ergänzt. Karten, App-Bilder und App-Texte wurden nicht verändert.
