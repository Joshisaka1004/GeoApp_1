# Prüfbericht: Karten 216, 218 und 221–225 / App DS78–DS84

Prüfer: Codex. Geprüft am 02.11.2026. Repository: [Joshisaka1004/GeoApp_1](https://github.com/Joshisaka1004/GeoApp_1). Geprüfter Commit: [edc8854b64ceea24575c5f4dba37828452d17ea3](https://github.com/Joshisaka1004/GeoApp_1/commit/edc8854b64ceea24575c5f4dba37828452d17ea3).

## Ergebnis und Umfang

**Die sieben vorhandenen Karten sind zeichnerisch und inhaltlich für die App geeignet. Ich habe keine mittleren oder großen geometrischen beziehungsweise zeichnerischen Fehler gefunden. Die sieben hinterlegten Antworten sind unabhängig bestätigt.**

Der Ordner heißt Karten_216-225, enthält jedoch ausdrücklich nur **216, 218 und 221–225**. Die Karten **217, 219 und 220** sind laut README nicht vorhanden und wurden deshalb nicht beurteilt.

Geprüft wurden 14 Originalkarten DE/EN, 14 App-Bilder DE/EN, die beiden Lösungstexte und die zweisprachigen App-Angaben, Fragen, Antworten, Hinweise und Lösungsschritte. Kleine gestalterische Abweichungen wurden entsprechend dem Prüfauftrag nicht beanstandet.

| Karte | App | Zeichnerisches Urteil | Bestätigtes Ergebnis |
|---|---|---|---|
| 216 – Zickzack zwischen zwei Kreisen | DS78 | Geeignet | 90° |
| 218 – Die Melone im Doppeltrog | DS79 | Geeignet | Rechte Waage +4,8 kg, also 2/3 = 66,666… % des Melonengewichts |
| 221 – Einmal rund um die Platte | DS80 | Geeignet | 12 · 0,75 m² = 9 m² |
| 222 – Der Blick am Beet vorbei | DS81 | Geeignet | Kleinster Winkel 60° |
| 223 – Platten rund um die Säule | DS82 | Geeignet | 96 Dreiecke + 48 Quadrate = 144 Platten |
| 224 – Der Steg zwischen den Teichen | DS83 | Geeignet | Mittelpunktsabstand 10 m; Steganteil 24/29 ≈ 82,75862 % |
| 225 – Der Stein kommt heim | DS84 | Geeignet | 10(√6+√2) m ≈ 38,63703 m |

## 216 – Zickzack zwischen zwei Kreisen

[App-Bild](https://github.com/Joshisaka1004/GeoApp_1/blob/edc8854b64ceea24575c5f4dba37828452d17ea3/Karten_216-225/App_Bilder/DS78.png)

Die beiden Kreise sind gleich groß dargestellt. M und N sind als Mittelpunkte erkennbar, P und Q liegen an den beiden gemeinsamen Schnittpunkten. Die 75°-Markierung gehört eindeutig zum Winkel PMQ. Die gezeichneten ersten beiden Geraden treffen die richtigen Marken A₁ und A₂ und verlaufen durch Q beziehungsweise P; die Pfeile passen dazu.

Die Zeichnung zeigt bewusst den Anfang der Konstruktion. Dass A₆ nicht vorweg eingezeichnet ist, ist kein Fehler. Der Text verwendet Geraden und schließt Marken in P oder Q aus, sodass die möglichen entarteten Schnittfälle ausgeschlossen sind. Die Frage stellt ausdrücklich klar, dass der Winkel bis 180° gemeint ist.

### Unabhängige Gegenprobe

Mit r=4, M=(0,0), N=(2r cos 37,5°;0) und P,Q=(r cos 37,5°; ±r sin 37,5°) wurden die zweiten Geraden-Kreis-Schnittpunkte tatsächlich berechnet, nicht nur die behauptete 105°-Drehung eingesetzt.

Für einen Durchgangspunkt H, den aktuellen Punkt A und den Zielkreismittelpunkt C ergibt sich der zweite Schnittpunkt als

H + t(A−H), mit t = −2(H−C)·(A−H) / |A−H|².

Bei **5.000 zufälligen zulässigen Startpunkten** liegt der Endwinkel nach sechs Schritten zwischen 89,9999999998° und 90,0000000001°. Die kleinen Abweichungen sind Rundungsfehler. Der konkrete Beispielstart mit Richtung 250° liefert A₆≈(−3,75877;1,36808), senkrecht zum Anfangsvektor. Auch die Rückkehr nach 24 Linien wurde bestätigt.

Die Erklärung über die Raute und die gleichsinnigen 105°-Drehungen der Radiusrichtungen ist konsistent. Die App-Antwort 90° stimmt.

## 218 – Melone, Wasserverteilung und Außenwandhöhe

[App-Bild DE](https://github.com/Joshisaka1004/GeoApp_1/blob/edc8854b64ceea24575c5f4dba37828452d17ea3/Karten_216-225/App_Bilder/DS79.png) · [App-Bild EN](https://github.com/Joshisaka1004/GeoApp_1/blob/edc8854b64ceea24575c5f4dba37828452d17ea3/Karten_216-225/App_Bilder/DS79_EN.png)

Die Darstellung unterscheidet die beiden Becken, die dünne Trennwand und die beiden Endauflager verständlich. Die waagrechten Maße 60 cm, 30 cm und 90 cm passen zusammen; die Breite von 40 cm ist separat angegeben. In der Lupe werden beide Wasserabstände **von derselben Trennwandoberkante** aus gemessen. Der größere Abstand von 35 mm gehört zum niedrigeren rechten Wasserstand.

### Warum der Wasserersatz richtig ist

Eine frei schwimmende Melone verdrängt Wasser mit genau ihrer eigenen Masse, hier **7,2 Liter**. Bei einem bestimmten ruhenden Wasserstand ist der Druck auf die benetzten Trogflächen derselbe wie bei einer vollständigen Wasserfüllung bis zu diesem Stand. Deshalb sind die auf den Trog übertragenen Kräfte und Momente dieselben wie nach einem entsprechenden Nachfüllen von Wasser.

Das lässt sich zusätzlich unmittelbar an der tatsächlichen Massenverteilung prüfen: Die schwimmende Melone fügt ihre Masse und ihr Moment hinzu; zugleich fehlt gegenüber einer gedachten Vollfüllung genau ihr verdrängtes Wasservolumen. Im horizontalen Moment heben sich diese beiden Beiträge auf. Die Lage der Melone im linken Becken beeinflusst die gesuchte Lastzunahme daher nicht.

### Wasserbilanz und rechte Waage

Bis zur Trennwandoberkante fehlen links 1,2 Liter und rechts 4,2 Liter, zusammen 5,4 Liter. Die übrigen 1,8 Liter entsprechen auf der gesamten Grundfläche 3600 cm² einer Höhe von **0,5 cm**. Der gemeinsame Endspiegel liegt also 5 mm über der Trennwand.

Gegenüber dem Anfang entsprechen die Laständerungen zwei waagrechten Wasserschichten:

| Becken | Spiegelanstieg | Äquivalente Zusatzmasse | Angriffsstelle von links |
|---|---:|---:|---:|
| links | 1 cm | 2,4 kg | 30 cm |
| rechts | 4 cm | 4,8 kg | 75 cm |

Zunahme der rechten Waage:

(2,4·30 + 4,8·75) / 90 = **4,8 kg = 2/3 des Melonengewichts**.

Als zusätzliche unabhängige Probe wurde ein tatsächlich ausgespartes kugelförmiges Melonenvolumen mit 7,2 Litern Verdrängung verwendet und die Masse sowie das Moment des verbleibenden Wassers zusammen mit der Melone bilanziert. Für Melonenpositionen bei 14, 22, 30, 38 und 46 cm von links ergibt sich jeweils rechts +4,8 kg und links +2,4 kg.

### Fehlt eine Angabe zur Außenwandhöhe?

**Nein, in der vorliegenden Fassung ist das ausreichend abgesichert.** Sowohl Originalkarte als auch App-Text sagen ausdrücklich, dass **kein Tropfen den Trog verlassen hat**. Zusammen mit dem angegebenen schwimmenden Endzustand schließt das eine zu niedrige Außenwand aus. Der Rand muss den Endspiegel 5 mm über der Trennwand zulassen. Eine zusätzliche numerische Außenwandhöhe wird für das Ergebnis nicht benötigt.

Ohne die Bedingung zum Wasserverlust wäre dies eine wichtige offene Annahme. Sie ist hier bereits vorhanden. Die Prozentumrechnung auf 66,67 % in der App ist korrekt.

## 221 – Überstrichene Fläche unabhängig vom Parkett-Argument geprüft

[App-Bild](https://github.com/Joshisaka1004/GeoApp_1/blob/edc8854b64ceea24575c5f4dba37828452d17ea3/Karten_216-225/App_Bilder/DS80.png)

F und M sind kongruent und gleich ausgerichtet. M liegt in der dargestellten Startlage mit einer Ecke an einer Kante von F, ohne F flächig zu überdecken. Die Zeichnung kennzeichnet die Dreiecksform ausdrücklich als Beispiel. Drehung und Umklappen werden im Text ausgeschlossen; ebenso wird die feste Fläche F ausdrücklich nicht mitgezählt. Damit sind die für das Ergebnis wesentlichen Bedingungen vollständig angegeben.

### Unabhängiger geometrischer Nachweis

Jedes nicht entartete Dreieck ist ein affines Bild des Referenzdreiecks

T = {(0,0),(1,0),(0,1)}.

Eine solche Abbildung erhält Verschiebungen, Berührung und Überdeckungsfreiheit und skaliert alle Flächen um denselben Faktor. Das Verhältnis „überstrichene Fläche / Dreiecksfläche“ kann deshalb an diesem einen Referenzdreieck bestimmt werden.

Die zulässigen Verschiebungsvektoren für eine berührende, nicht überdeckende Kopie liegen auf dem Rand des Differenzsechsecks T−T. Für jede seiner sechs Kanten wurde die gesamte kontinuierliche Schiebung berechnet: Ihre überstrichene Fläche ist die konvexe Hülle der beiden übersetzten Enddreiecke.

Die Vereinigung dieser sechs Flächen hat:

- Dreiecksfläche 0,5;
- überstrichene Fläche 6;
- äußere Hüllfläche 6,5;
- ausgesparte innere Fläche genau T mit Fläche 0,5.

Das Verhältnis ist also **6/0,5=12**. Die feste Dreiecksfläche wird nicht mitgezählt. Durch die affine Übertragung gilt dies für jede Dreiecksform.

Eine zusätzliche Gegenprobe mit **200 zufälligen Dreiecken** sowie einem ausdrücklich sehr flachen, stumpfwinkligen Dreieck ergibt durchgehend Faktor 12. Damit sind die Formunabhängigkeit und **9 m²** unabhängig von der mitgelieferten Parkettzählung bestätigt. Auch die Parketterklärung selbst stimmt.

## 222 – Laufrichtung, Sichtstrahlen und Minimum

[App-Bild DE](https://github.com/Joshisaka1004/GeoApp_1/blob/edc8854b64ceea24575c5f4dba37828452d17ea3/Karten_216-225/App_Bilder/DS81.png) · [App-Bild EN](https://github.com/Joshisaka1004/GeoApp_1/blob/edc8854b64ceea24575c5f4dba37828452d17ea3/Karten_216-225/App_Bilder/DS81_EN.png)

Die Bahnrichtung ist gegen den Uhrzeigersinn eingezeichnet. Der blaue Richtungspfeil bei Lena ist die vorwärts gerichtete Tangente; die gelben Strahlen sind die beiden streifenden Sichtgrenzen des Beets. Die α-Markierung gehört zum kleineren Winkel zwischen der Laufrichtung und dem günstigeren Sichtstrahl. O und M sowie Radius 40 m, Abstand 14 m und Beetradius 6 m sind eindeutig zugeordnet.

Die gezeichnete Lena-Position ist eine Beispielposition. Sie muss nicht die Stelle mit dem globalen Minimum zeigen; gefragt ist ausdrücklich das Minimum über die ganze Runde.

### Unabhängige Winkelrechnung

Für einen Bahnpunkt P=40(cos θ,sin θ), Laufrichtung f=(−sin θ,cos θ), Beetmitte M=(0,14) und Abstand d=|M−P| ist der kleinere mögliche Sichtwinkel

α(θ) = Winkel(f,M−P) − arcsin(6/d).

Damit wurde die gesamte Runde abgetastet und das Minimum anschließend lokal optimiert. Ergebnis:

- Minimum **60°**;
- optimale Stelle P=(20√3,20)≈(34,64102;20);
- Winkel am beetnächsten Bahnpunkt ≈76,65764°;
- Winkel am beetfernsten Bahnpunkt ≈83,62063°.

Die Werte passen zur Lösung. Die untere Schranke arccos((14+6)/40)=60° wird an der Tangente durch den von O fernsten Beetpunkt tatsächlich erreicht. Kein Widerspruch zwischen Bild, Bedingungen und Rechnung.

## 223 – Zwölfecke und Plattenzahl

[App-Bild](https://github.com/Joshisaka1004/GeoApp_1/blob/edc8854b64ceea24575c5f4dba37828452d17ea3/Karten_216-225/App_Bilder/DS82.png)

Außenkontur und Säule sind beide regelmäßige Zwölfecke mit gemeinsamer Mitte und parallelen entsprechenden Seiten. Die Seitenlängen 3 m und 1 m sind passend markiert; das Maßverhältnis ist stimmig. Die Plattensymbole unterscheiden Quadrat und gleichseitiges Dreieck. Die blau gefärbte Bodenfläche spart die graue Säule aus.

Aus den direkt berechneten regelmäßigen Polygonflächen ergibt sich

Boden = 3(2+√3)(3²−1²) = **48+24√3 m²**.

Mit b Quadraten und a gleichseitigen Dreiecken der Kantenlänge 1 m gilt b+a√3/4=48+24√3. Wegen der Irrationalität von √3 folgen eindeutig **b=48** und **a=96**, zusammen **144**.

Der Text sichert die Existenz eines solchen unzerschnittenen Belags ausdrücklich zu. Für die gesuchte Stückzahl ist keine Bestimmung einer bestimmten Verlegung erforderlich. Die allgemeine Fläche und die Plattenbilanz stimmen; eine vollständige Suche aller möglichen Beläge war nicht Bestandteil dieser Prüfung.

## 224 – Berührung und zusammenhängender Steg

[App-Bild DE](https://github.com/Joshisaka1004/GeoApp_1/blob/edc8854b64ceea24575c5f4dba37828452d17ea3/Karten_216-225/App_Bilder/DS83.png) · [App-Bild EN](https://github.com/Joshisaka1004/GeoApp_1/blob/edc8854b64ceea24575c5f4dba37828452d17ea3/Karten_216-225/App_Bilder/DS83_EN.png)

Das Rechteck hat das richtige Verhältnis 16:18. Die Teiche berühren ihre jeweiligen beiden Eckmauern und einander. Die Diagonale AC trifft den gemeinsamen Berührpunkt; der Steg ist dort zusammenhängend. Die kurzen Landabschnitte bei A und C sind als solche dargestellt. Der Hinweis, dass die Radien im Bild nur Beispielwerte sind, verhindert eine unzulässige Maßentnahme.

### Eigene Schnittrechnung

Mit A=(0,0), C=(16,18), M₁=(r₁,r₁), M₂=(16−r₂,18−r₂) und s=r₁+r₂ erzwingt die äußere Berührung

(16−s)²+(18−s)²=s².

Die geometrisch zulässige Lösung ist **s=10**; s=58 passt nicht in das Rechteck. Damit beträgt der Mittelpunktsabstand 10 m und der Verbindungsvektor (6,8).

Zusätzlich wurden die Schnittintervalle der Diagonale X(t)=t(16,18), 0≤t≤1, mit beiden Kreisen direkt über quadratische Gleichungen berechnet:

- erster Teich: t von r₁/58 bis r₁/10;
- zweiter Teich: t von 1−r₂/10 bis 1−r₂/58.

Weil r₁+r₂=10 ist, treffen die beiden Intervalle bei t=r₁/10 genau zusammen. Der gesamte Steganteil ist daher

1−(r₁+r₂)/58 = **24/29 ≈82,75862 %**.

Eine numerische Probe mit **61 zulässigen Radienpaaren** zwischen (2,8) und (8,2) bestätigt denselben Anteil und das genaue Zusammentreffen der Intervalle. Die App fragt bewusst nur Teil b) in Prozent ab; Teil a) bleibt im Lösungsweg. Das ist korrekt umgesetzt.

## 225 – Sechseck und sechs Drehungen

[App-Bild DE](https://github.com/Joshisaka1004/GeoApp_1/blob/edc8854b64ceea24575c5f4dba37828452d17ea3/Karten_216-225/App_Bilder/DS84.png) · [App-Bild EN](https://github.com/Joshisaka1004/GeoApp_1/blob/edc8854b64ceea24575c5f4dba37828452d17ea3/Karten_216-225/App_Bilder/DS84_EN.png)

Die Pfosten A bis F sind auf dem regelmäßigen Sechseck tatsächlich gegen den Uhrzeigersinn beschriftet. Die 10 m beziehen sich auf eine Sechseckseite. Der kleine Drehungsausschnitt zeigt einen 30°-Bogen gegen den Uhrzeigersinn; „vorher“ und „nachher“ sowie die Pfeilrichtung passen zusammen. Die Reihenfolge A→B→C→D→E→F ist ausdrücklich angegeben. Der unbekannte Startpunkt wird im Bild nicht vorweggenommen.

Die sechs Drehungen wurden unabhängig direkt rückwärts und vorwärts berechnet. Mit A=(10,0) und den weiteren Pfosten bei Winkeln 60°,120°,… ergibt sich der Start

P≈(−27,32050808;10).

Seine Entfernung von A ist **38,63703305 m = 10(√6+√2) m**. Die Vorwärtsprobe landet nach genau den sechs vorgeschriebenen Drehungen wieder in A; die numerische Abweichung beträgt nur rund 4·10⁻¹⁵ m.

Die gesamte Abbildung ist eine Punktspiegelung mit Zentrum Z=(−5√3,5), also auf dem Umkreis bei 150°. Damit sind auch das in der Lösung verwendete Zentrum und die Selbstumkehr der Gesamtabbildung bestätigt. Die App-Antwort 38,64 m ist richtig gerundet.

## App-Bilder und Zweisprachigkeit

Diesmal liegen für alle sieben App-Zeichnungen deutsche und englische Fassungen vor. Die englischen Bilder tragen passend übersetzte Legenden und Bildtexte. DS78 benötigt keine übersetzten Legenden, weil diese Zeichnung nur sprachunabhängige Punktnamen und die Winkelangabe enthält.

Beim Wechsel von der vollständigen Karte zum App-Bild bleiben die für die Aufgaben wichtigen Zahlen, Punkte, Pfeile und Legenden erhalten. Ich sehe in den betrachteten Originalgrößen keine abgeschnittene wesentliche Beschriftung und keinen mittleren oder großen Beschriftungszusammenstoß.

Die Anpassungen an die numerische App-Eingabe sind konsistent:

- 218: 2/3 wird als Prozentzahl 66,67 eingegeben.
- 224: Gefragt ist nur Teil b), ebenfalls in Prozent, mit 82,76.
- Die übrigen fünf Karten behalten ihre numerischen Antworten mit passenden Einheiten.

## Nachweise und Prüfgrenzen

- **32 Quelldateien** wurden über die GitHub-Verbindung heruntergeladen und anhand ihrer Git-Blob-Prüfsummen mit dem genannten Commit verglichen: 28 PNGs und vier Textdateien.
- Alle Originalkarten wurden in Übersichten betrachtet; die App-Bilder in Originalgröße. Die beiden besonders zur Prüfung genannten Originalkarten 218 und 221 wurden zusätzlich vollständig in Originalgröße geprüft.
- Die beiden Lösungstexte und der vollständige zweisprachige App-Textauszug wurden gelesen. Alle sieben Antworten wurden durch eigene Rechnungen beziehungsweise Simulationen kontrolliert.
- Die numerischen Zufallsproben ergänzen die geometrischen Argumente. Bei 221 folgt die allgemeine Formunabhängigkeit aus der affinen Übertragung, nicht aus den Zufallsproben allein.
- Die Prüfung betrifft die bereitgestellten Bilder und Textdaten. Zeichenskripte oder separate Lösungsbild-PNGs sind für diese Serie nicht enthalten. Die laufende App und ihre Darstellung auf unterschiedlichen Geräten wurden nicht bedient oder vermessen.

**Keine Korrektur der sieben vorhandenen Karten oder ihrer Antworten erforderlich.** Karten 217, 219 und 220 bleiben mangels Dateien ungeprüft. Dieser Bericht wurde auf Wunsch im Repository ergänzt; Karten, App-Bilder und App-Texte wurden dabei nicht verändert.
