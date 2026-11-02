"""GR 15: Die Waage im Quadratrahmen – Grün = 28 (Seite 10, gegenüberliegende Rahmenstücke 13 und 23)."""
from gemeinsam import *  # noqa: F401,F403
from scipy.optimize import brentq
from shapely.geometry import Polygon as SP

A, B, C, D = P(0, 0), P(10, 0), P(10, 10), P(0, 10)
RHO, PHI = math.sqrt(14), 20.0


def innen(dy):
    m = P(5.3, 5 + dy)
    return m, [m + RHO * P(math.cos(math.radians(w + PHI)), math.sin(math.radians(w + PHI))) for w in (225, 315, 45, 135)]


DY = brentq(lambda dy: SP([A, B, innen(dy)[1][1], innen(dy)[1][0]]).area - 13, -2, 1)
M, (E, F, Gq, H) = innen(DY)


def grund(ax, gruen, zahlen=True):
    G.flaeche(ax, [A, B, C, D], "white")
    G.flaeche(ax, [E, F, Gq, H], gruen)
    for p, q in ((A, E), (B, F), (C, Gq), (D, H)):
        G.linie(ax, p, q)
    for p in (A, B, C, D, E, F, Gq, H):
        G.punkt(ax, p, 6)
    masslinie(ax, B, A, "10", 0.9, 26)
    if zahlen:
        G.text(ax, (6.3, 0.95), "13", 28)
        G.text(ax, (4.3, 8.65), "23", 28)


def frage(ax, sp):
    grund(ax, GRUEN)
    G.text(ax, M, "?", 38)
    return D, C


def loesung(ax, sp):
    grund(ax, HGRUEN)
    for poly, f in (([M, B, F], HBLAU), ([M, D, H], HBLAU), ([M, A, E], "#FCD9B8"), ([M, C, Gq], "#FCD9B8")):
        G.flaeche(ax, poly, f, rand=False)
    for q in (A, B, C, D):
        strich(ax, M, q, GRAU, 1.6)
    strich(ax, E, Gq, GRAU, 1.6)
    strich(ax, F, H, GRAU, 1.6)
    G.punkt(ax, M, 6)
    G.text(ax, M + P(0, -1.05), "28", 26, "#1E8A45")
    return None


erzeuge(15,
        dict(DE=("Grün = ?", "zwei Quadrate; die Zahlen innen sind Flächen"),
             EN=("Green = ?", "two squares; the numbers inside are areas"), zeichne=frage),
        dict(DE=("Lösung: Grün = 100 − 2 · 36 = 28", "Gegenüber = halber Rahmen; blaue und orange Zwickel gleich groß"),
             EN=("Solution: Green = 100 − 2 · 36 = 28", "opposite = half the frame; blue and orange slivers are equal"),
             zeichne=loesung))
