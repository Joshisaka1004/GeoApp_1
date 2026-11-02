"""GR 05: Die Leitern durch den Kusspunkt – x = 12 (Strecken 20 und 15 durch den Berührpunkt)."""
from gemeinsam import *  # noqa: F401,F403

GRUEN_D = "#1E9A4B"

r, R = 4.5, 8.0
A, B = P(0, 0), P(2 * math.sqrt(r * R), 0)
O1, O2 = P(0, r), P(B[0], R)
T = O1 + r / (r + R) * (O2 - O1)
E1, E2 = P(B[0], 2 * R), P(0, 2 * r)
F = P(B[0], -2 * r)


def grund(ax, fc="white"):
    G.linie(ax, P(-4, 0), P(21, 0))
    kreis(ax, O1, r, fc=fc, z=3)
    kreis(ax, O2, R, fc=fc, z=3)
    G.linie(ax, A, E1)
    G.linie(ax, B, E2)


def frage(ax, sp):
    grund(ax)
    G.linie(ax, A, B, lw=6, farbe=ROT)
    G.text(ax, (6, -1.1), "x", 34, ROT)
    masslinie(ax, A, E1, "20", 3.2, farbe=BLAU, lw=2, anteil=0.2)
    masslinie(ax, E2, B, "15", 3.2, farbe=GRUEN_D, lw=2, anteil=0.6)
    for p in (A, B, T, E1, E2):
        G.punkt(ax, p)
    return P(14.5, 0), P(20.5, 0)


def loesung(ax, sp):
    grund(ax, fc="none")
    G.flaeche(ax, [A, E1, F], HGELB, rand=False)
    G.linie(ax, A, E1)
    G.linie(ax, A, B, lw=6, farbe=ROT)
    strich(ax, A, E2)
    strich(ax, F, E1)
    strich(ax, A, F, BLAU, 2.4)
    G.rechter_winkel(ax, T, A, B, 0.7)
    G.rechter_winkel(ax, A, E1, F, 0.7)
    G.text(ax, (-1.1, 4.5), "9", 22)
    G.text(ax, (13.1, 8.0), "16", 22)
    G.text(ax, (13.1, -4.5), "9", 22)
    G.text(ax, (4.6, -5.6), "15", 24, BLAU)
    G.text(ax, (6.6, -1.0), "x", 30, ROT)
    for p in (A, B, T, E1, E2, F):
        G.punkt(ax, p)
    return None


erzeuge(5,
        dict(DE=("x = ?", "Die Kreise berühren sich und die Linie"), EN=("x = ?", "The circles touch each other and the line"), zeichne=frage),
        dict(DE=("Lösung: x = 12", "rechter Winkel in T, 15er-Strecke nach unten schieben: 20 · 15 = 25 · x"),
             EN=("Solution: x = 12", "right angle at T, slide the 15 down:  20 · 15 = 25 · x"),
             zeichne=loesung))
