# Lösungen Karten 211–214 (#Jochen V.)

## Karte 211 – Die Segel am Ovalteich

**Gegeben:** sechs Punkte am Ufer eines Ovals (vier Pfosten A, B, C, D und zwei Laternenplätze P1, P2) und sieben Segelflächen. **Gesucht:** die Fläche des blauen Segels PBD bei P2.

**Antwort: 14 m².**

1. **Die falsche Fährte.** Man möchte die Teichform, die Pfostenlagen und die Laternenplätze bestimmen und dann rechnen. Dafür fehlen Angaben, und selbst mit Annahmen wird es zäh.

2. **Zurück zum Kreis.** Eine gleichmäßige Dehnung in einer Richtung macht aus dem Kreis das Oval und vergrößert jede Fläche im selben Faktor. Vergleicht man Produkte aus je zwei Flächen, kürzt sich dieser Faktor. Man darf sich also einen Kreis mit Radius R denken.

3. **Fläche aus drei Seiten.** Im Kreis sieht man die Sehne XY vom Uferpunkt P aus unter einem Winkel, dessen Sinus XY/(2R) ist. Daraus folgt für jedes Segel: Fläche PXY = PX · PY · XY / (4R).

4. **Aha: Alles Unbekannte kürzt sich.** Das Produkt der roten Flächen ist PA·PB·AB · PC·PD·CD / (16R²). Das Produkt der blauen ist PA·PC·AC · PB·PD·BD / (16R²). Im Quotienten kürzen sich alle Abstände zur Laterne und der Radius R. Übrig bleibt AB·CD / (AC·BD), und das hängt nur noch von den festen Pfosten ab. Das Produkt der roten Flächen geteilt durch das Produkt der blauen ist also an jeder Uferstelle derselbe Wert.

5. **Rechnen.** Bei P1 ist (64 · 6) / (12 · 48) = 384 / 576 = 2/3. Bei P2 muss dasselbe gelten: (28 · 8) / (24 · x) = 2/3. Daraus folgt x = 224 · 3 / (2 · 24) = **14 m²**.

6. **Probe.** Der Teich x²/100 + y²/25 = 1 mit A(10 | 0), B(−6 | 4), C(−8 | −3), D(6 | −4), P1(−6 | −4), P2(8 | −3) liefert genau diese sieben Flächen und bei P2 für PBD genau 14 m². Die Laterne kann beliebig am Ufer wandern, das Verhältnis bleibt 2/3.

**Kurz gesagt:** Gegeben sind sieben Flächen, die Lösung ist die achte: Das blaue Segel PBD misst **14 m²**.

## Karte 212 – Der Rahmen ohne Schachtel

**Gegeben:** In den Schalen liegen 17 Teile mit 0 Nasen, 59 mit 1 Nase, ungezählt viele mit 2 Nasen, 49 mit 3 Nasen und 7 mit 4 Nasen. Das Bild ist ein Rechteck, das Format ist unbekannt. **Gesucht:** die Zahl der Teile mit mindestens einer geraden Kante (die Randteile, Ecken eingeschlossen).

**Antwort: 56 Teile.**

1. **Die falsche Fährte.** Man möchte zuerst das Format ermitteln und dann 2·Breite + 2·Höhe − 4 rechnen. Aber die Gesamtzahl der Teile ist unbekannt, weil eine Schale fehlt, und selbst mit ihr wüsste man nicht, wie die Teile auf Reihen und Spalten verteilt sind.

2. **Aha 1: Es gibt genau so viele Löcher wie Nasen.** Jede Fuge zwischen zwei Nachbarteilen besteht aus genau einer Nase und genau einem Loch. Zählt man die Fugen einmal von der Nasenseite und einmal von der Lochseite, kommt dieselbe Zahl heraus.

3. **Seiten zählen.** Jedes Teil hat 4 Seiten, und jede ist Nase, Loch oder gerade Kante. Über alle Teile gilt: 4 · (Teile) = Nasen + Löcher + gerade Kanten = 2 · Nasen + gerade Kanten. Also bringt jedes Teil **4 − 2 · (seine Nasen)** gerade Kanten ein:

   | Nasen | 0 | 1 | **2** | 3 | 4 |
   |---|---|---|---|---|---|
   | gerade Kanten je Teil | +4 | +2 | **0** | −2 | −4 |

4. **Aha 2: Die ungezählte Schale spielt keine Rolle.** Sie trägt genau 0 bei. Gerade Kanten insgesamt = 4 · 17 + 2 · 59 − 2 · 49 − 4 · 7 = 68 + 118 − 98 − 28 = **60**.

5. **Die Ecken-Falle.** Ein Randteil ohne Ecke hat genau 1 gerade Kante, jede der 4 Ecken hat 2. Also ist die Zahl der geraden Kanten = Randteile + 4, und es gibt 60 − 4 = **56** Randteile.

**Probe:** Die 60 geraden Kanten bilden den Umfang, also ist Breite + Höhe = 30. Wären zum Beispiel 84 Teile in der ungezählten Schale, hätte das Puzzle 216 Teile im Format 12 × 18. Dann sind es 59 + 2 · 84 + 3 · 49 + 4 · 7 = 402 Nasen und 12 · 17 + 18 · 11 = 402 Fugen, passt. Randteile: 2 · 12 + 2 · 18 − 4 = 56.

**Zugabe:** Das Format selbst lässt sich nicht bestimmen. Alle zehn Formate von 6 × 24 (144 Teile) bis 15 × 15 (225 Teile) sind möglich, und jedes davon hat 56 Randteile.

**Kurz gesagt:** Gegeben sind die Zahlen in den Schalen, die Lösung ist die Anzahl der Randteile: **56**.

## Karte 213 – Der Sandtisch an der Mauer

**Gegeben:** Eine Dreieckplatte mit den Seiten 13 dm, 14 dm und 15 dm. Die 14-dm-Seite liegt an der Mauer, die beiden anderen Kanten sind frei. Die Sandoberfläche steigt höchstens 3 auf 4. Es wird gesiebt, bis nichts mehr liegen bleibt. **Gesucht:** die größte Sandhöhe und die Sandmenge in Litern.

**Antwort: 45 cm an der höchsten Stelle (direkt an der Mauer) und 126 Liter.**

1. **Die falsche Fährte.** Wie viel Sand gesiebt wurde und wie lange, steht nirgends. Das braucht man auch nicht: Gefragt ist der Endzustand, in dem kein Körnchen mehr liegen bleibt.

2. **Aha 1: Der Endzustand ist der höchstmögliche Haufen.** An einer freien Kante ist die Sandhöhe 0. Geht man von einem Punkt P geradeaus zur nächsten freien Kante, fällt die Oberfläche auf je 4 cm höchstens um 3 cm. Also liegt der Sand bei P höchstens ¾ · (Abstand von P zur nächsten freien Kante) hoch. Weil überall weiter Sand fällt, bis nichts mehr hält, wird diese Grenze überall genau erreicht. Die Mauer zählt dabei nicht mit, an ihr fällt nichts herunter.

3. **Die Scheinlösung.** Ohne Mauer wäre der Haufen eine Pyramide über dem Punkt, der von allen drei Kanten gleich weit entfernt ist. Dieser Abstand ist der Inkreisradius r = 4 dm. Das ergäbe 30 cm Höhe und ⅓ · 84 dm² · 3 dm = 84 Liter. Die Mauer ändert aber alles.

4. **Aha 2: Die Mauer ist ein Spiegel.** Man spiegelt die Platte an der Mauer. So entsteht ein Drachenviereck mit vier freien Kanten (15, 13, 13, 15), und die Mauer liegt auf seiner Symmetrieachse. Ein Haufen auf diesem Drachen wäre spiegelgleich, nichts flösse quer über die Achse. Unser Haufen ist also genau die halbe Ladung des Drachens.

5. **Aha 3: Ein Drachen hat einen Inkreis.** Bei ihm sind die Summen der Gegenseiten gleich (15 + 13 = 13 + 15). Sein Haufen ist deshalb eine Pyramide über dem Inkreismittelpunkt D. Der Punkt D liegt auf der Mauer, und zwar dort, wo die Winkelhalbierende aus C sie trifft: 7,5 dm von A und 6,5 dm von B entfernt.
   - Die Platte hat 84 dm². Sie zerfällt in die Dreiecke 9-12-15 und 5-12-13, beide mit der Höhe 12 dm auf der Mauerseite.
   - Der Drachen ist also 168 dm² groß und hat den halben Umfang 28 dm.
   - Damit ist sein Inkreisradius ρ = 168 : 28 = 6 dm.
   - Die Sandhöhe in D ist ¾ · 6 dm = **4,5 dm = 45 cm**.

6. **Volumen.** Die Pyramide über dem Drachen hat das Volumen ⅓ · 168 dm² · 4,5 dm = 252 dm³. Die Hälfte davon liegt auf der Platte: **126 dm³ = 126 Liter**. Die Mauer bringt also genau 50 % mehr Sand als die Scheinlösung.

**Probe:** Die Strecke CD teilt die Platte in die Dreiecke ACD mit 45 dm² und BCD mit 39 dm². Über jedem steigt der Sand gleichmäßig von 0 an der freien Kante bis 4,5 dm in D. Jedes Stück ist eine schiefe Pyramide mit dem Volumen Fläche · 4,5 : 3. Das ergibt 67,5 + 58,5 = 126 dm³. Außerdem hat D von AC und von BC jeweils genau 6 dm Abstand.

**Kurz gesagt:** Gegeben ist die Platte mit der Mauer, die Lösung sind zwei Zahlen: **45 cm Höhe und 126 Liter Sand.**

## Karte 214 – Immer geradeaus

**Gegeben:** ein Würfel mit 8 cm Kante, der Anfang M in der Mitte der unteren Vorderkante und die Richtung „4 cm nach rechts, 3 cm nach oben“. **Gesucht:** die Bandlänge bis das Band zum ersten Mal wieder in M ankommt und dort in derselben Richtung weiterlaufen würde.

**Antwort: 160 cm** (genau 20 Kantenlängen).

1. **Die falsche Fährte.** Wer das Band Fläche für Fläche im Raum verfolgt, braucht 28 Teilstücke mit krummen Brüchen. Das geht, ist aber mühsam und fehleranfällig.

2. **Aha 1: Den Würfel abrollen.** Man stellt den Würfel mit der Vorderseite auf den Tisch und kippt ihn jedes Mal über die Kante, die das Band gerade erreicht. Weil das Band nicht zur Seite biegt, druckt es dabei eine einzige gerade Linie auf den Tisch. Die Flächen liegen in einem Kästchengitter aus 8-cm-Quadraten. Die Linie beginnt bei (4 | 0) und steigt um 3 je 4 nach rechts.

3. **Die nächste gleiche Stelle.** Auf dieser Geraden sucht man den nächsten Punkt, der wieder die Mitte einer waagrechten Gitterlinie ist. Bei 8 cm Höhe liegt die Gerade bei x = 4 + 32/3, bei 16 cm bei 4 + 64/3, erst bei 24 cm bei x = 36. Das ist der Punkt (36 | 24), und die Strecke bis dahin ist √(32² + 24²) = **40 cm**. Ein 3-4-5-Dreieck macht die Zahl glatt.

4. **Wo am Würfel ist das?** Man rollt mit: vorn 5 cm, rechts 8⅓ cm, oben 1⅔ cm, hinten 10 cm, unten 1⅔ cm, links 8⅓ cm, vorn 5 cm (zusammen 40 cm). Dann quert das Band die **Mitte der oberen Vorderkante** und läuft von vorn auf die Oberseite, wieder „4 vor, 3 weg von der Kante, nach rechts“.

5. **Aha 2: Eine Vierteldrehung.** Dreht man den Würfel eine Vierteldrehung um die Achse durch die Mitten der linken und der rechten Fläche, wird aus der Unterseite die Vorderseite und aus der Vorderseite die Oberseite. Die untere Vorderkante wird zur oberen Vorderkante, rechts bleibt rechts. Diese Drehung bringt die Anfangslage genau auf die Lage nach 40 cm. Weil Punkt und Richtung den weiteren Verlauf festlegen, sind die nächsten 40 cm das gedrehte Bild der ersten 40 cm. Das wiederholt sich: Nach 40, 80 und 120 cm quert das Band die Mitten der oberen Vorderkante, der oberen Hinterkante und der unteren Hinterkante. Erst nach vier Vierteldrehungen ist es wieder an der unteren Vorderkante.

6. **Nicht früher.** In derselben Richtung durch M kann das Band im Abrollbild nur an der Mitte einer waagrechten Gitterlinie laufen. An einer senkrechten Linie wäre das Verhältnis 3 : 4 vertauscht. Solche Stellen kommen nur alle 40 cm, und nach 40, 80 und 120 cm liegt jeweils eine andere Kante darunter.

7. **Antwort:** Das Band ist **160 cm** lang, genau 20 Kantenlängen.

**Probe:** 4 · (5 + 8⅓ + 1⅔ + 10 + 1⅔ + 8⅓ + 5) = 4 · 40 = 160. Es sind 28 Teilstücke: je 5 auf Vorderseite, Oberseite, Hinterseite und Unterseite (je 23⅓ cm) und je 4 auf linker und rechter Seite (je 33⅓ cm). 4 · 23⅓ + 2 · 33⅓ = 160.

**Zugabe:** Das Band kreuzt sich 16-mal. Mit der Marke bei 4 cm entstünde das bekannte Sechseck mit 24√2 ≈ 33,9 cm, bei 2 cm wären es 16√5 ≈ 35,8 cm.

**Kurz gesagt:** Gegeben sind der Würfel und die Richtung, die Lösung ist die Bandlänge: **160 cm**.
