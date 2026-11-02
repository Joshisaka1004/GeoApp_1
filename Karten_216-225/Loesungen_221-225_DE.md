# Lösungen Karten 221–225 (#Jochen V.)

## Karte 221 – Einmal rund um die Platte

**Ergebnis: 12 · 0,75 m² = 9 m²** – für jedes Dreieck mit dieser Fläche.

**Die scheinbar fehlende Größe** ist die Form des Dreiecks: keine Seite, kein Winkel, keine Höhe ist gegeben. Der Weg kommt ohne sie aus.

1. **Das Parkett.** Dreht man F um 180° um die Mitte einer Seite, bilden F und das gedrehte Dreieck ein Parallelogramm. Setzt man das fort, entsteht für jedes Dreieck ein lückenloses Parkett aus Platten dieser Form, abwechselnd „aufrecht“ (wie F, nur verschoben) und „umgedreht“ (um 180° gedreht). Wegen α + β + γ = 180° stoßen an jeder Ecke 6 Platten zusammen.
2. **Wo kann M liegen?** M ist eine verschobene Kopie von F und darf F nicht überdecken, muss F aber berühren. Es gibt sechs aufrechte Parkettplatten, die F in genau einer Ecke berühren (an jeder Ecke von F zwei). Zwischen zwei benachbarten schiebt Mia M entlang einer Plattenkante um genau eine Kantenlänge; M berührt F immer und überdeckt es nie. Eine andere Bahn gibt es nicht: Die Berührlagen bilden genau den Rand des Sechsecks aller Verschiebungen „Punkt von F minus Punkt von F“.
3. **Was überstreicht eine Schiebung?** Schiebt man M um eine Kantenlänge e entlang einer eigenen Kantenrichtung, überstreicht M Anfangslage, Endlage und das Parallelogramm dazwischen: T + e·h = T + 2T = **3T** (e·h ist die doppelte Dreiecksfläche). Im Parkett sind das genau drei Platten: Anfang, Ende und eine umgedrehte Platte dazwischen.
4. **Sechs Schiebungen:** 6 · 3T = 18T. Jede Eckenlage ist doppelt gezählt (als Ende und als Anfang), das sind 6T zu viel: 18T − 6T = **12T**. Gezählt sind die 6 aufrechten Eckenlagen und die 6 umgedrehten Zwischenplatten.

**Kontrolle durch Zählen:** M überstreicht genau die 12 Parkettplatten, die F berühren. An jeder Ecke von F liegen 5 weitere Platten: 3 · 5 = 15; die 3 Platten, die an einer Kante von F liegen, sind doppelt gezählt: 15 − 3 = 12.

12 · 0,75 m² = **9 m²**. (Nebenbei: Für ein Quadrat oder einen Kreis wäre der Faktor 8, beim Dreieck ist es 12. Würde M umgeklappt, hinge das Ergebnis von der Form ab – deshalb „nie umgeklappt“.)

## Karte 222 – Der Blick am Beet vorbei

**Ergebnis: α = 60°** (genau; cos α = (OM + r)/R = 20/40).

1. **Winkel wird zum Bogen.** Lenas Laufrichtung berührt die Bahn in ihrem Standpunkt P. Trifft ein Blickstrahl die Bahn ein zweites Mal in X, so ist der Winkel zwischen Laufrichtung und Sehne PX halb so groß wie der Bogen von P nach X, der vor Lena liegt (Sehnen-Tangenten-Winkel). Dieser Bogen ist mindestens so groß wie der kürzere Bogen der Sehne. Liegt die Sehne im Abstand h von O, gilt daher: α ≥ arccos(h/R).
2. **Nur der fernste Beetpunkt zählt.** Trifft der Blickstrahl das Beet, enthält die Gerade einen Beetpunkt. Kein Beetpunkt ist weiter als OM + r = 20 m von O entfernt, also ist h ≤ 20 m und damit α ≥ arccos(20/40) = 60°.
3. **Gleichheit wird erreicht.** Die Gerade, die das Beet in seinem von O am weitesten entfernten Punkt F berührt, steht senkrecht auf OF und hat genau den Abstand 20 m von O. Von ihren beiden Bahnpunkten aus liegt für genau einen der kürzere Bogen vorn. Dort sieht Lena den Beetrand unter genau 60° zur Laufrichtung. (Bei O = (0|0), M = (0|14): Lena steht bei (20√3 | 20) ≈ (34,6 | 20), ihr Blick streift das Beet bei (0 | 20).)
4. **Das Minimum liegt an einer überraschenden Stelle:** weder am beetnächsten Punkt der Bahn (≈ 76,7°) noch am beetfernsten (≈ 83,6°). Das Ergebnis hängt nur von OM + r ab, nicht davon, wie sich die 20 m auf Abstand und Beetradius verteilen.

## Karte 223 – Platten rund um die Säule

**Ergebnis: 144 Platten** (96 dreieckige und 48 quadratische).

**Falsche Fährte:** Man versucht, den Boden wirklich zu belegen und die Platten zu zählen. Das ist mühsam und fehleranfällig, und der Boden lässt viele verschiedene Beläge zu.

**Aha:** Die Anzahl hängt gar nicht vom Belag ab. Ein Quadrat hat die Fläche 1 (rational), ein Dreieck die Fläche √3/4 (ein rationales Vielfaches von √3). Weil √3 irrational ist, müssen der rationale Teil und der √3-Teil der Bodenfläche für sich stimmen.

1. **Fläche eines Zwölfecks mit Seite s:** Es besteht aus 12 gleichschenkligen Dreiecken mit 30° an der Spitze. Aus R² = s²/(2 − 2·cos 30°) = s²(2 + √3) folgt die Fläche 12 · ½ · R² · sin 30° = 3(2 + √3) · s².
2. **Boden:** 3(2 + √3)(3² − 1²) = 24(2 + √3) = 48 + 24√3 m².
3. **Bilanz:** Bei a Dreiecken und b Quadraten gilt a·√3/4 + b = 48 + 24√3, also (a/4 − 24)·√3 = 48 − b. Wäre a/4 − 24 ≠ 0, so wäre √3 ein Bruch. Also a = 96 und b = 48.
4. **Gesamtzahl:** 96 + 48 = **144 Platten**.

Lage, Anordnung und Drehung der Platten spielen keine Rolle; der Text sichert zu, dass der Belag möglich ist. (Eine Suche über alle Beläge zeigt: Es gibt sie wirklich – 6 verschiedene, alle mit 96 Dreiecken und 48 Quadraten.)

## Karte 224 – Der Steg zwischen den Teichen

**Ergebnis: a) 10 m  b) 24/29 ≈ 82,8 %** – für jede Größe der beiden Teiche.

**Gemeinsamer Gedanke: Der Pfeil von Mitte zu Mitte ist immer derselbe.**

**a)** Die Radien seien r₁ und r₂, ihre Summe s = r₁ + r₂. Mit A als Ursprung liegen die Mittelpunkte bei M₁ = (r₁ | r₁) und M₂ = (16 − r₂ | 18 − r₂). Der Pfeil von M₁ nach M₂ ist daher (16 − s | 18 − s): Er hängt nur von s ab, nicht von der Aufteilung auf die beiden Radien. Weil die Teiche sich berühren, ist er s lang:
(16 − s)² + (18 − s)² = s², also s² − 68s + 580 = 0, s = 10 (die zweite Lösung 58 passt nicht in den Hof).
Die Mittelpunkte sind also immer **10 m** voneinander entfernt, und der Pfeil zeigt stets 6 m quer und 8 m längs.

**b)** *Aha 1:* Der Berührpunkt liegt auf M₁M₂ im Abstand r₁ von M₁: T = (r₁ | r₁) + (r₁/10)·(6 | 8) = r₁·(1,6 | 1,8) – ein Vielfaches von (16 | 18). T liegt also **immer auf dem Weg AC**; der Weg geht im Berührpunkt direkt von einem Teich in den anderen über, der Steg ist ein einziges Stück.

*Aha 2:* Eine Sehne, die von einem Kreispunkt T ausgeht und mit dem Durchmesser durch T den Winkel φ einschließt, ist 2r·cos φ lang. Die Durchmesser durch T liegen beide auf der Linie M₁M₂, also bildet der Weg mit beiden denselben Winkel φ. Die Steglänge ist 2r₁·cos φ + 2r₂·cos φ = 2·10·cos φ, das Doppelte der Projektion des festen Pfeils (6 | 8) auf den Weg: 2·(6·16 + 8·18)/√580 = 480/√580 m.
Der Weg ist √580 m lang. Steganteil = 480/580 = **24/29 ≈ 82,8 %**, egal wie groß die einzelnen Teiche sind. (Beispiel r₁ = 3, r₂ = 7: Steg ≈ 19,93 m von ≈ 24,08 m.)

## Karte 225 – Der Stein kommt heim

**Ergebnis: 10·(√6 + √2) m ≈ 38,64 m** (= 4R·cos 15° mit R = 10 m).

1. **Rückwärts denken.** Gesucht ist ein Start, der nach sechs Drehungen in A endet. Rückwärts sind das sechs Drehungen um F, E, D, C, B, A um −30° – das sieht nach sechs unhandlichen Schritten aus.
2. **Gesamtdrehung 6 · 30° = 180°.** Zwei Drehungen ergeben wieder eine Drehung, deren Winkel die Summe ist. Sechs Drehungen mit zusammen 180° ergeben deshalb eine **Punktspiegelung** an einem festen Punkt Z. Eine Punktspiegelung ist ihre eigene Umkehrung.
3. **Aha:** Wegen „zweimal spiegeln = nichts“ ist „Von welchem Start komme ich in A an?“ dasselbe wie „Wohin komme ich, wenn ich in A starte?“. Rückwärts ist gleich vorwärts. (Startet der Stein in A, bleibt er bei der ersten Drehung um A liegen; nur fünf Drehungen sind zu verfolgen.)
4. **Das Zentrum Z finden.** Mit komplexen Zahlen sei w = e^{iπ/6} (also w⁶ = −1) und v_k = R·w^{2k} die Pfosten. Die k-te Drehung ist z ↦ v_k + w(z − v_k). Hintereinander ergibt das F(z) = w⁶·z + (1 − w)·Σ v_k·w^{5−k}. Die Summe ist R·w⁵·Σ w^k = 2R·w⁵/(1 − w), denn Σ w^k = (1 − w⁶)/(1 − w) = 2/(1 − w). Also F(z) = −z + 2R·w⁵ = −z − 2R·e^{−iπ/6}, und das Zentrum ist Z = −R·e^{−iπ/6} = R·e^{i150°}: ein Punkt auf dem Umkreis, genau die Bogenmitte zwischen C und D.
5. **Der Start.** Aus F(P) = A folgt P = 2Z − A, also AP = 2·AZ.
6. **Die Länge.** Z liegt auf dem Umkreis mit ∠AOZ = 150°; deshalb AZ = 2R·sin 75° = 2R·cos 15°. Es folgt AP = 4R·cos 15° = 10(√6 + √2) ≈ **38,64 m**. (Koordinaten mit O im Ursprung, A = (10 | 0): P = (−27,32 | 10).)

Probe: Dreht man P nacheinander um A, B, C, D, E, F um je 30° gegen den Uhrzeigersinn, landet man genau auf A. (Mit Drehung im Uhrzeigersinn oder umgekehrter Reihenfolge käme 14,14 m heraus – deshalb nennt der Text beides.)
