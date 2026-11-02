# Lösungen Karten 215–220 (#Jochen V.)

## Karte 218 – Die Melone im Doppeltrog

**Gegeben:** Ein Trog, innen 90 cm × 40 cm, mit senkrechten Wänden. Eine dünne Trennwand bei 60 cm teilt ihn in ein linkes Becken (60 cm) und ein rechtes (30 cm). Das Wasser steht links 5 mm, rechts 35 mm unter der Trennwandkante. Eine 7,2 kg schwere Melone schwimmt frei im linken Becken. Die Waagen stehen unter den beiden Enden. **Gesucht:** die Zunahme der rechten Waage als Bruchteil des Melonengewichts.

**Antwort: 2/3** (4,8 kg der 7,2 kg; links kommen nur 2,4 kg hinzu).

1. **Die falsche Fährte.** Die Melone schwimmt in der Mitte des linken Beckens, 30 cm von der linken Waage entfernt. Mit dem Hebelgesetz bekäme die rechte Waage 30/90 = **1/3** ihres Gewichts, die linke 2/3. Das klingt überzeugend, ist aber falsch, denn die Melone liegt gar nicht auf dem Trog. Wer an Archimedes denkt und sagt, das verdrängte Wasser verteile sich gleichmäßig, kommt auf 1/2. Auch das stimmt nicht.

2. **Aha 1: Der Trog spürt die Melone nur über das Wasser.** Die Melone berührt weder Boden noch Wände. Auf den Trog drückt allein das Wasser, und sein Druck hängt nur davon ab, wie tief eine Stelle unter dem Wasserspiegel liegt. Denkt man sich die Melone weg und gießt stattdessen Wasser nach, bis der Spiegel genauso hoch steht, drückt auf jeden Quadratzentimeter des Trogs genau dasselbe. Die Melone wirkt also wie **7,2 Liter Wasser, die man bis zum neuen Spiegel nachfüllt**. Wo sie schwimmt, ist egal.

3. **Aha 2: Wohin kommen die 7,2 Liter?** Bis zur Trennwandkante fehlen links 60 · 40 · 0,5 = 1200 cm³ = 1,2 Liter und rechts 30 · 40 · 3,5 = 4200 cm³ = 4,2 Liter, zusammen 5,4 Liter. Das ist weniger als 7,2 Liter. Beide Becken laufen also voll, das Wasser steht über der Trennwand und hat überall denselben Spiegel. Die restlichen 1,8 Liter verteilen sich auf die ganze Fläche von 90 · 40 = 3600 cm², also steht der Spiegel am Ende **5 mm über der Kante**. Dieser Endzustand hängt nicht davon ab, wie die Melone hineinkam oder ob zwischendurch etwas über die Trennwand schwappte.

4. **Zuwachs in jedem Becken.** Links steigt das Wasser von 5 mm unter bis 5 mm über die Kante, also um 1 cm: 2400 cm² · 1 cm = 2,4 Liter. Rechts steigt es von 35 mm unter bis 5 mm über die Kante, also um 4 cm: 1200 cm² · 4 cm = 4,8 Liter. Zusammen sind das 7,2 Liter, genau das Melonengewicht.

5. **Erst jetzt der Hebel.** Jede Zunahme ist eine waagrechte Schicht zwischen senkrechten Wänden und wirkt deshalb in der Mitte ihres Beckens:
   - links bei 30 cm: Die rechte Waage bekommt 30/90 · 2,4 kg = 0,8 kg.
   - rechts bei 75 cm: Die rechte Waage bekommt 75/90 · 4,8 kg = 4,0 kg.
   - Zusammen kommen rechts **4,8 kg = 2/3** des Melonengewichts hinzu, links nur 2,4 kg = 1/3.

6. **Probe.** Das Gesamtmoment um die linke Waage ist 2,4 · 30 + 4,8 · 75 = 432 kg·cm = 7,2 kg · 60 cm. Die Melone wirkt also genau so, als läge sie **fest auf der Trennwand**, 60 cm von links, obwohl sie 30 cm weiter links schwimmt. Eine Computer-Simulation mit Wasser, kugelförmiger Melone und verschiedenen Schwimmlagen im linken Becken ergibt jedes Mal 4,8 kg rechts.

**Kurz gesagt:** Gegeben sind der Trog und die Melone, die Lösung ist ein Bruch: Auf der rechten Waage kommen **2/3** des Melonengewichts hinzu, genau umgekehrt wie die Hebel-Rechnung verspricht.

## Karte 216 – Zickzack zwischen zwei Kreisen

**Gegeben:** zwei gleich große Kreise um M und N, die sich in P und Q kreuzen, mit Winkel PMQ = 75°. Die Zickzacklinie läuft von A0 durch Q nach A1, durch P nach A2, durch Q nach A3 und so weiter bis A6. **Gesucht:** der Winkel A0MA6 mit Scheitel M.

**Antwort: 90°** – egal, wo Mia beginnt.

1. **Die falsche Fährte.** Man möchte A1, A2, … A6 der Reihe nach ausrechnen. Dafür fehlt aber die Lage von A0, und selbst mit Koordinaten wird es eine lange Rechnung mit krummen Zahlen. Eine zweite Falle ist der Gedanke, dass Hinweg über Q und Rückweg über P sich gegenseitig aufheben.

2. **Die Raute.** Weil beide Kreise den Radius r haben, sind MP, MQ, NP und NQ alle gleich lang, also ist MPNQ eine Raute. Bei M hat sie 75°, also bei P (und Q) 180° − 75° = **105°**.

3. **Aha 1: Der Zeiger ist ein Spiegelbild.** Man denkt sich in jedem Kreis einen Uhrzeiger vom Mittelpunkt zur aktuellen Marke. Die erste Linie g geht durch A0 und Q, beide liegen auf dem Kreis um M. Das Dreieck MA0Q ist also gleichschenklig (MA0 = MQ = r), und seine Symmetrieachse ist das Lot von M auf g. Spiegelt man an diesem Lot, wird **der Zeiger M→A0 zum Spiegelbild des Zeigers M→Q**. Genauso ist das Dreieck NA1Q gleichschenklig, und **N→A1 ist das Spiegelbild von N→Q**, gespiegelt am Lot von N auf g.

4. **Was der Spiegel mit dem Winkel macht.** Beide Lote stehen senkrecht auf derselben Geraden g, die beiden Spiegelachsen sind also parallel. Für die Richtungen der Zeiger ist es deshalb derselbe Spiegel. Ein Spiegel erhält Winkel, kehrt aber den Drehsinn um.
   - Vorher: M→Q liegt 105° gegen den Uhrzeigersinn weiter als N→Q (das ist der Rautenwinkel bei Q, im Bild ist M links oben und N rechts oben von Q).
   - Nachher: N→A1 liegt 105° gegen den Uhrzeigersinn weiter als M→A0.

   **Mit der ersten Linie dreht sich der Zeiger also um 105° gegen den Uhrzeigersinn.** Wo g genau liegt, spielt keine Rolle, denn die Lage der Spiegelachse fällt heraus.

5. **Aha 2: Der Rückweg dreht weiter, nicht zurück.** Für die zweite Linie durch A1 und P gilt dasselbe mit P: M→A2 ist das Spiegelbild von M→P und N→A1 das Spiegelbild von N→P, wieder an parallelen Achsen. Bei P liegt N→P 105° gegen den Uhrzeigersinn weiter als M→P (P liegt oben, M links unten, N rechts unten). Nach dem Spiegeln liegt M→A2 105° gegen den Uhrzeigersinn weiter als N→A1. Auch diese Linie dreht den Zeiger also um **105° in dieselbe Richtung**. Das gilt für jede weitere Linie, egal wo Mia angefangen hat.

6. **Zusammensetzen.** Nach sechs Linien hat sich der Zeiger um 6 · 105° = 630° = 360° + 270° gedreht. Der Zeiger M→A6 steht also 270° gegen den Uhrzeigersinn hinter M→A0, und das sind von der anderen Seite gesehen 90°. Damit ist **Winkel A0MA6 = 90°**.

**Probe:** Mit r = 4, M(0 | 0) und N(6,347 | 0) liegen die Marken, gemessen als Richtung vom jeweiligen Mittelpunkt, bei A0 250°, A1 355°, A2 100°, A3 205°, A4 310°, A5 55° und A6 160°, jeder Schritt sind also genau +105°. A6 = (−3,759 | 1,368), und die Strecken MA0 und MA6 stehen senkrecht aufeinander, denn (−1,368) · (−3,759) + (−3,759) · 1,368 = 0. Für 20 000 zufällige Startpunkte ergibt die Rechnung jedes Mal 90,000000000°.

**Zugabe:** Alle zwei Linien rückt die Marke auf dem Kreis um M um 210° = 7 · 30° weiter. Die Marken A0, A2, A4, … sind deshalb Ecken eines regelmäßigen Zwölfecks, das sternförmig angelaufen wird. Zum ersten Mal zurück in A0 ist Mia nach 24 Linien, und der Zeiger hat dann genau 7 volle Umdrehungen gemacht.

**Kurz gesagt:** Gegeben sind zwei gleiche Kreise und der Winkel 75°, die Lösung ist der Winkel bei M: Jede Linie dreht den Zeiger um 105°, sechs Linien ergeben 630°, und der Winkel A0MA6 beträgt **90°**.
