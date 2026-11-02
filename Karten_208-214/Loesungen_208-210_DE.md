# Lösungen Karten 208–210 (#Jochen V.)

## Karte 208 – Die Bogenfliesen

**Ergebnis: 2400 cm²** – genau 6 Fliesenflächen, ganz ohne π.

1. **Die falsche Fährte.** Man möchte die Fläche innerhalb der roten Linie ausrechnen und den blauen Kreis (100π cm²) abziehen. Die rote Linie hat aber zwanzig Ein- und Ausbuchtungen. Kaum eine ganze Fliese liegt innen, überall entstehen Bruchstücke mit π. Das geht, ist aber lang und fehleranfällig.

2. **Zerlegen.** Die zwei Bögen einer Fliese teilen sie in drei Stücke: zwei Viertelkreise mit je π·10²/4 = 25π cm² und ein S-förmiges Band mit 400 − 50π cm². Zwei Viertelkreise und ein Band ergeben zusammen genau eine Fliese. Die Schlaufen laufen nur auf Bögen, also besteht die gelbe Fläche aus ganzen Stücken.

3. **Aha: Jedes Band bringt seine zwei Viertelkreise mit.** Jeder Bogen trennt einen Viertelkreis von einem Band. Folgt man einer geschlossenen Linie, dreht man sich an jedem Bogen um eine Vierteldrehung, insgesamt aber genau um eine volle Drehung. Deshalb haben von den Bögen jeder geschlossenen Linie genau 4 mehr ihren Viertelkreis innen als ihr Band innen.
   - Die rote Linie gibt der gelben Fläche 4 überzählige Viertelkreise (12 gegen 8).
   - Die blaue Linie zeigt der gelben Fläche bei allen 4 Bögen ihre Bandseite und nimmt ihr damit genau 4 wieder weg.
   - Jedes Band wird von zwei Bögen begrenzt, jeder Viertelkreis von einem. Rechnet man das durch, kommen in der gelben Fläche auf jedes Band genau zwei Viertelkreise.
   - Also ist die gelbe Fläche genau so viele Fliesen groß, wie sie Bänder enthält.

4. **Zählen.** Die gelbe Fläche enthält 6 Bänder, nämlich in den sechs Fliesen der Spalten 2 bis 4 von links und der Zeilen 4 und 5 von unten (Zählung ab 1), dazu 12 Viertelkreise in den Randfliesen:
   6 · (400 − 50π) + 12 · 25π = **2400 cm²**.

5. **Probe.** Ersetzt man jeden Bogen durch seine Sehne, wird die rote Linie zu einem Vieleck mit 6,5 Fliesen und der blaue Kreis zu einer Raute mit 0,5 Fliesen. Die Differenz ist wieder 6 Fliesen = 2400 cm².

**Zugabe:** Jede einzelne geschlossene Linie dieser Art umschließt „ganze Zahl + π/4“ Fliesen: hier rot 6 + π/4, blau π/4. Erst die Differenz zweier Linien ist eine ganze Zahl.

## Karte 209 – Hundert Punkte im Park

**Gegeben:** Lina hat am Ende genau 100 Punkte. **Gesucht:** die Station, an der sie dann steht.

**Antwort: Station C.** Die 100 ist die Angabe, nicht die Lösung. Nur an Station C kann man genau 100 Punkte haben; an jeder anderen Station ist das unmöglich.

1. **Zwei Wege, zwei Ergebnisse.** A→E→B→C bringt −2 + 6 + 18 = 22 Punkte, A→H→C bringt 18 + 17 = 35 Punkte. Die Route ist also nicht egal, aber die beiden Werte unterscheiden sich um genau 13.

2. **Die versteckte Höhe.** Man geht einmal um jede der acht dreieckigen Rasenflächen herum: Die Punkte heben sich jedes Mal genau auf. Nur die Runde um den Brunnen bringt gegen den Uhrzeigersinn **+13** (B→E→D→C→B: −6 + 23 + 14 − 18). Ohne den Brunnen hätte jede Station einen festen „Wert“, wie eine Höhe. Man rechnet ihn auf Wegen aus, die den Brunnen nicht umrunden:

   | Station | A | B | C | D | E | F | G | H |
   |---|---|---|---|---|---|---|---|---|
   | Wert | 0 | 4 | 22 | 21 | −2 | 20 | 15 | 5 |

   Probe: Bei 13 der 16 Schilder ist die Zahl genau der Wertunterschied der beiden Stationen. Nur A–H, H–D und D–C weichen um genau 13 ab.

3. **Die Größe, die sich nie ändert.** Bei jedem Schritt ändert sich „Punktestand minus Wert der aktuellen Station“ um 0 oder um ±13. Diese Differenz ist also immer ein Vielfaches von 13. An Station X kann man deshalb nur den Punktestand „Wert(X) + Vielfaches von 13“ haben.

4. **Der Rest entscheidet.** Die Reste der Werte bei Teilung durch 13 sind: A 0, B 4, **C 9**, D 8, E 11, F 7, G 2, H 5. Alle acht sind verschieden. Weil 100 = 7 · 13 + 9 ist, hat der Punktestand 100 den Rest 9. Dazu passt nur **C**. Jede andere Station bräuchte einen anderen Rest (A 0, B 4, D 8, E 11, F 7, G 2, H 5), also kann Lina dort nicht mit 100 Punkten stehen.

5. **Probe: 100 Punkte an C gibt es wirklich.** A→E→B→C bringt 22 Punkte. Danach läuft Lina sechsmal die Runde C→B→E→D→C, das sind je +13. Sie steht dann an C mit 22 + 6 · 13 = 22 + 78 = **100 Punkten**. Der kürzeste mögliche Gang dorthin hat 22 Wegstücke: fünfmal um den Außenrand (je +13), dann A→H→C. Der Punktestand fällt dabei nie unter 0.

**Kurz gesagt:** 100 Punkte hat Lina laut Aufgabe. Die Lösung ist die Station: **C**.

**Zugabe:** Mit 101, 103, 105, 107 oder 110 Punkten könnte Lina an keiner Station stehen. Fünf der dreizehn Reste kommen nirgends vor.

## Karte 210 – Der Riesenball im Lampenlicht

**Ergebnis: Der Ball ist 3,2 m gerollt. Die Schattenfläche beträgt 15π/4 m² ≈ 11,78 m².**
(Nebenbei: Die Lampe hängt in 3,6 m Höhe; diese Zahl steht nicht im Text.)

1. **Der Schattenkegel.** Die Strahlen, die den Ball gerade streifen, bilden einen geraden Kreiskegel mit der Spitze in der Lampe L. Der Ball steckt darin und berührt ihn ringsum. Der Schatten ist der Schnitt dieses Kegels mit dem Boden.

2. **Aha 1 – die Kugel unter dem Boden.** Man denkt sich den Boden aus Glas und den Kegel darunter verlängert. Darunter passt genau eine zweite Kugel (Radius R), die den Kegel ringsum und den Boden von unten berührt. Der Ball berührt den Boden in T, die untere Kugel in S.
   - Für jeden Randpunkt P des Schattens ist PT gleich dem Stück der Mantellinie bis zum Berührkreis des Balls, denn alle Tangenten von P an eine Kugel sind gleich lang. Ebenso ist PS gleich dem Stück bis zum unteren Berührkreis.
   - Also ist PT + PS gleich dem festen Abstand der beiden Berührkreise: Der Schatten ist eine Ellipse mit den Brennpunkten T und S.

3. **Aha 2 – Breite gleich Produkt der Radien.** Im Längsschnitt durch L und den Ball seien A und B die Schattenenden. Im Dreieck LAB ist der Ball der Inkreis, die untere Kugel der Ankreis gegenüber L.
   - In A halbieren AI und AJ den Innen- und den Außenwinkel, also ist ∠IAJ = 90°.
   - Daraus folgt tan(α/2) = r/AT und cot(α/2) = R/AS, also **r·R = AT·AS**.
   - Die Tangentenabschnitte sind gleich: AS = BT. Damit gilt r·R = AT·BT = (a − c)(a + c) = **b²**. Das Quadrat der halben Schattenbreite ist das Produkt der beiden Radien.

4. **Aha 3 – die Erhaltungsgröße.** Die Streckung mit Zentrum L bildet den Ball auf die untere Kugel ab, mit Faktor R/r. Die Mittelpunkte liegen r über und R unter dem Boden. Für die Lampenhöhe h gilt daher h + R = (R/r)(h − r), also **2/h = 1/r − 1/R**. R hängt nur von h und r ab, nicht davon, wo der Ball liegt. Beim Rollen wird der Schatten länger, aber **nie breiter oder schmaler**.

5. **Start.** Der Kreis mit Ø 3 m ergibt b = 1,5 m für immer. Mit r = 1 folgt R = b²/r = 2,25 m (und h = 3,6 m).

6. **Fläche.** a = 2,5 m und b = 1,5 m, also Fläche = π·a·b = **15π/4 m² ≈ 11,78 m²**.

7. **Rollweg (rückwärts).** Die Streckung von L aus, auf den Boden projiziert, führt T in S über: OS = (R/r)·OT = 9/4·d. Damit ist TS = 5/4·d. Aus der Ellipse folgt c = √(a² − b²) = 2, also TS = 4 und **d = 3,2 m**.

**Probe:** Lampe L(0|3,6), Ballmitte (3,2|1). Die Gerade durch L und (2,7|0) hat vom Ballmittelpunkt den Abstand 1, ebenso die Gerade durch L und (7,7|0). Die Schattenlänge ist 7,7 − 2,7 = 5. Der Startkreis hat den Radius 3,6 · 5/12 = 1,5.
