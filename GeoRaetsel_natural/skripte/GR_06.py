"""GR 06: Die Waage im schiefen Viereck – Zeige: A = B + C + 3 · D (Punkt auf der Unterseite, Diagonalenmitten)."""
from gemeinsam import *  # noqa: F401,F403
from shapely.geometry import Polygon as SP

K, L, M, N = P(2, 0), P(7, 0), P(11, 8), P(0, 6)
Pp = P(4, 0)
E, F = (K + M) / 2, (L + N) / 2
ROT_D, BLAU_D, GRUEN_D = "#C62828", "#1F5FBF", "#1E8A45"


def grund(ax, blau, gruen, rot):
    G.flaeche(ax, [Pp, M, N], blau, rand=False)
    G.flaeche(ax, [Pp, N, K], gruen, rand=False)
    G.flaeche(ax, [Pp, L, M], gruen, rand=False)
    G.flaeche(ax, [Pp, E, F], rot, rand=True)
    for p, q in ((K, L), (L, M), (M, N), (N, K), (Pp, N), (Pp, M)):
        G.linie(ax, p, q)
    G.linie(ax, K, M, lw=1.6, farbe="#333333")
    G.linie(ax, L, N, lw=1.6, farbe="#333333")
    gleich_bei(ax, K, E, 0.16, 1)
    gleich_bei(ax, E, M, 0.2, 1)
    gleich_bei(ax, L, F, 0.3, 2)
    gleich_bei(ax, F, N, 0.25, 2)
    for p in (Pp, E, F):
        G.punkt(ax, p)


def frage(ax, sp):
    grund(ax, HBLAU, HGRUEN, ROT)
    G.text(ax, (4.6, 5.7), "A", 34, BLAU_D)
    G.text(ax, (1.75, 2.1), "B", 30, GRUEN_D)
    G.text(ax, (7.35, 2.4), "C", 30, GRUEN_D)
    G.text(ax, (4.75, 3.05), "D", 22, "white")
    ax.plot([0], [-4.6], alpha=0)                      # Platz für den Rahmen unter der Figur
    farbformel(ax.figure, 865, [("A", BLAU_D), (" = ", G.INK), ("B", GRUEN_D), (" + ", G.INK), ("C", GRUEN_D),
                                (" + 3 · ", G.INK), ("D", ROT_D)])
    return P(11, 8), P(0, 6)


def loesung(ax, sp):
    grund(ax, "#E8F1FC", "#E6F6EA", HROT)
    for q in (K, L):
        G.punkt(ax, q, 5)
    strich(ax, K, F, ROT, 2.2)
    strich(ax, F, M, ROT, 2.2)
    ax.annotate("", xy=(2.2, -0.55), xytext=(6.8, -0.55),
                arrowprops=dict(arrowstyle="<|-|>", color=ROT, lw=2, mutation_scale=18))
    G.text(ax, (4.5, -1.3), "P", 22, ROT)
    ax.plot([0], [-4.6], alpha=0)
    z = {"DE": ("P gleitet: alles ändert sich gleichmäßig, also nur die Ecken prüfen",
                "dort gilt  4 · D = großes − kleines Dreieck"),
         "EN": ("P slides: everything changes evenly, so check only the corners",
                "there  4 · D = big − small triangle")}[sp]
    ax.figure.text(0.5, 1 - 850 / 1100, z[0], ha="center", va="center", fontsize=20, color=G.INK)
    ax.figure.text(0.5, 1 - 895 / 1100, z[1], ha="center", va="center", fontsize=20, color=G.INK)
    return None


erzeuge(6,
        dict(DE=("Zeige:", "beliebiges Viereck, beliebiger Punkt;  A ist nur das Blau"), EN=("Prove:", "any quadrilateral, any point;  A is the blue part only"), zeichne=frage),
        dict(DE=("Lösung: Punkt an die Ecken schieben", "Mitten der Diagonalen halbieren zweimal"),
             EN=("Solution: slide the point to the corners", "the diagonal midpoints halve twice"),
             zeichne=loesung))
