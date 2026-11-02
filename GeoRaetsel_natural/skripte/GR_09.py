"""GR 09: Zwei Dächer im Trapez – Grün = 25 (Flächen 18, 8, 27, 9)."""
from gemeinsam import *  # noqa: F401,F403

A, B, C, D = P(0, 0), P(17.5, 0), P(11, 8), P(0, 8)
Pp, R = P(7.5, 0), P(5, 8)
X, Y = P(3, 4.8), P(155 / 16, 5)


def grund(ax, gruen):
    G.flaeche(ax, [Pp, B, Y], gruen, rand=False)
    for p, q in ((A, B), (B, C), (C, D), (D, A), (A, R), (B, R), (D, Pp), (C, Pp)):
        G.linie(ax, p, q)
    G.rechter_winkel(ax, A, B, D, 0.42)
    G.rechter_winkel(ax, D, A, C, 0.42)
    for p in (Pp, R):
        G.punkt(ax, p)


def frage(ax, sp):
    grund(ax, GRUEN)
    G.text(ax, (3.55, 1.55), "18", 30)
    G.text(ax, (2.75, 6.95), "8", 30)
    G.text(ax, (6.35, 4.5), "27", 30)
    G.text(ax, (8.55, 7.0), "9", 30)
    G.text(ax, (11.4, 1.6), "?", 34)
    return D, R


def loesung(ax, sp):
    G.flaeche(ax, [Pp, X, R], HGELB, rand=False)
    G.flaeche(ax, [Pp, Y, R], "#FCE3C8", rand=False)
    grund(ax, HGRUEN)
    strich(ax, Pp, R, ROT, 2.6)
    G.text(ax, (3.55, 1.55), "18", 24)
    G.text(ax, (2.75, 6.95), "8", 24)
    G.text(ax, (1.1, 4.4), "12", 20, GRAU)
    G.text(ax, (5.15, 4.6), "12", 20, ROT)
    G.text(ax, (7.45, 4.6), "15", 20, ROT)
    G.text(ax, (8.55, 7.0), "9", 24)
    G.text(ax, (13.3, 3.6), "15", 20, GRAU)
    G.text(ax, (11.4, 1.6), "25", 30, "#1E8A45")
    return None


erzeuge(9,
        dict(DE=("Grün = ?", "Die Zahlen sind Flächen"), EN=("Green = ?", "The numbers are areas"), zeichne=frage),
        dict(DE=("Lösung: Grün = 25", "18 · 8 = 12²;  27 − 12 = 15;  Grün · 9 = 15²"),
             EN=("Solution: Green = 25", "18 · 8 = 12²;  27 − 12 = 15;  Green · 9 = 15²"),
             zeichne=loesung))
