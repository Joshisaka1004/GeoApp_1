"""GR 07: Die feste Dachspitze – x = 18° (78° + 42° = 120°, AB = CD, gleichseitiges Dach auf AD)."""
from gemeinsam import *  # noqa: F401,F403

d = math.radians
B, C = P(0, 0), P(10, 0)
A = 4.5 * P(math.cos(d(78)), math.sin(d(78)))
D = P(10 - 4.5 * math.cos(d(42)), 4.5 * math.sin(d(42)))
v = D - A
E = A + P(v[0] * math.cos(d(60)) - v[1] * math.sin(d(60)), v[0] * math.sin(d(60)) + v[1] * math.cos(d(60)))


def grund(ax, x_farbe):
    for p, q in ((A, B), (B, C), (C, D), (D, A), (A, E), (E, D), (E, C)):
        G.linie(ax, p, q)
    G.gleich(ax, A, B, 1, laenge=0.45)
    G.gleich(ax, C, D, 1, laenge=0.45)
    for p, q in ((A, D), (A, E), (E, D)):
        G.gleich(ax, p, q, 2, laenge=0.45)
    G.winkel(ax, B, C, A, 1.5, "78°", HBLAU, abstand=0.62, groesse=20)
    G.winkel(ax, C, B, D, 1.7, "42°", HBLAU, abstand=0.6, groesse=18)
    G.winkel(ax, C, D, E, 2.0, "x", x_farbe, abstand=0.78, groesse=22)
    for p in (A, B, C, D, E):
        G.punkt(ax, p)


def frage(ax, sp):
    grund(ax, ORANGE)
    return B, C


def loesung(ax, sp):
    G.flaeche(ax, [E, A, B], HGELB, rand=False)
    G.flaeche(ax, [E, D, C], HGELB, rand=False)
    grund(ax, ORANGE)
    strich(ax, E, B, ROT, 2.4)
    G.gleich(ax, E, B, 3, laenge=0.45)
    G.gleich(ax, E, C, 3, laenge=0.45)
    G.gleich(ax, B, C, 3, laenge=0.45)
    G.winkel(ax, B, E, A, 3.4, "18°", None, abstand=0.8, groesse=18)
    G.text(ax, E + P(0.2, -1.6), "60°", 20, ROT)
    return None


erzeuge(7,
        dict(DE=("x = ?", ""), EN=("x = ?", ""), zeichne=frage),
        dict(DE=("Lösung: x = 60° − 42° = 18°", "60°-Drehung um die Spitze: gelbe Dreiecke gleich, unten auch gleichseitig"),
             EN=("Solution: x = 60° − 42° = 18°", "60° turn about the apex: yellow triangles equal, bottom one equilateral"),
             zeichne=loesung))
