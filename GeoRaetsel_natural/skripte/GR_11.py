"""GR 11: Der Knick in der Mitte – x = 58° (Rechteck, E Mitte von BC, AE ⊥ EF, 64° bei F)."""
from gemeinsam import *  # noqa: F401,F403

t = math.tan(math.radians(32))
w, h = 4.0, 8 * t
A, B, C, D = P(0, 0), P(w, 0), P(w, h), P(0, h)
E = P(w, h / 2)
F = P(w * (1 - t * t), h)
Gp = P(2 * w, h)                       # Verlängerung von AE trifft die verlängerte Oberseite


def grund(ax, x_farbe):
    for p, q in ((A, B), (B, C), (C, D), (D, A), (A, E), (E, F), (A, F)):
        G.linie(ax, p, q)
    G.gleich(ax, B, E, 1, laenge=0.28)
    G.gleich(ax, E, C, 1, laenge=0.28)
    G.rechter_winkel(ax, E, A, F, 0.3)
    G.winkel(ax, F, D, A, 0.75, "64°", HBLAU, abstand=0.62, groesse=20)
    G.winkel(ax, E, B, A, 0.85, "x", x_farbe, abstand=0.62, groesse=24)
    for p in (A, E, F):
        G.punkt(ax, p)


def frage(ax, sp):
    grund(ax, ORANGE)
    return A, F


def loesung(ax, sp):
    G.flaeche(ax, [A, F, Gp], HGELB, rand=False)
    grund(ax, ORANGE)
    strich(ax, C, Gp)
    strich(ax, E, Gp, ROT, 2.4)
    strich(ax, F, Gp, ROT, 2.4)
    G.gleich(ax, A, E, 2, laenge=0.28)
    G.gleich(ax, E, Gp, 2, laenge=0.28)
    G.gleich(ax, F, Gp, 3, laenge=0.28)
    G.gleich(ax, A, F, 3, laenge=0.28)
    G.winkel(ax, A, B, E, 1.25, "32°", None, abstand=0.72, groesse=15)
    G.winkel(ax, A, E, F, 1.55, "32°", None, abstand=0.76, groesse=15)
    G.winkel(ax, Gp, F, A, 1.55, "32°", None, abstand=0.7, groesse=15)
    G.punkt(ax, Gp)
    return None


erzeuge(11,
        dict(DE=("x = ?", "Rechteck"), EN=("x = ?", "rectangle"), zeichne=frage),
        dict(DE=("Lösung: x = 90° − 32° = 58°", "verlängern: gelbes Dreieck gleichschenklig, die Linie halbiert 64°"),
             EN=("Solution: x = 90° − 32° = 58°", "extend: the yellow triangle is isosceles, the line halves 64°"),
             zeichne=loesung))
