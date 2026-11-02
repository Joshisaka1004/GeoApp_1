"""GR 08: Halb, Drittel, Viertel – Rot : Blau = 1 : 1 (Innendreieck = Eckdreieck = 1/10)."""
from gemeinsam import *  # noqa: F401,F403

A, B, C = P(4, 8), P(0, 0), P(12, 0)
D = (B + C) / 2
E, E2 = C + (A - C) / 3, C + 2 * (A - C) / 3
F, F2, F3 = A + (B - A) / 4, A + (B - A) / 2, A + 3 * (B - A) / 4
X, Y, Z = P(42 / 5, 12 / 5), P(24 / 5, 24 / 5), P(28 / 5, 8 / 5)


def grund(ax, rot, blau):
    G.flaeche(ax, [X, Y, Z], rot, rand=False)
    G.flaeche(ax, [B, D, Z], blau, rand=False)
    for p, q in ((A, B), (B, C), (C, A), (A, D), (B, E), (C, F)):
        G.linie(ax, p, q)
    G.gleich(ax, B, D, 1, laenge=0.4)
    G.gleich(ax, D, C, 1, laenge=0.4)
    for p, q in ((C, E), (E, E2), (E2, A)):
        G.gleich(ax, p, q, 2, laenge=0.4)
    for p, q in ((A, F), (F, F2), (F2, F3), (F3, B)):
        G.gleich(ax, p, q, 3, laenge=0.4)
    for p in (D, E, F):
        G.punkt(ax, p)
    for p in (E2, F2, F3):
        G.punkt(ax, p, 5)


def frage(ax, sp):
    grund(ax, ROT, BLAU)
    return P(9.6, 0), P(11.8, 0)


def loesung(ax, sp):
    G.flaeche(ax, [C, D, Z], HBLAU, rand=False)
    grund(ax, HROT, HBLAU)
    strich(ax, C, Z, BLAU, 2.4)
    G.gleich(ax, A, Y, 1, laenge=0.35)
    G.gleich(ax, Y, Z, 1, laenge=0.35)
    G.gleich(ax, C, X, 2, laenge=0.35)
    G.gleich(ax, X, Y, 2, laenge=0.35)
    G.text(ax, (6.3, 2.95), "1/10", 15, ROT)
    G.text(ax, (3.9, 0.55), "1/10", 15, BLAU)
    G.text(ax, (7.75, 0.55), "1/10", 15, BLAU)
    return None


erzeuge(8,
        dict(DE=("Rot : Blau = ?", ""), EN=("Red : Blue = ?", ""), zeichne=frage),
        dict(DE=("Lösung: Rot : Blau = 1 : 1", "Blau = Hilfsdreieck rechts;  Rot: doppelte Grundseite, halbe Höhe"),
             EN=("Solution: Red : Blue = 1 : 1", "Blue = helper triangle on the right;  Red: double base, half height"),
             zeichne=loesung))
