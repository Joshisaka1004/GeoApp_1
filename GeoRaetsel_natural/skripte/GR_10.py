"""GR 10: Der Kreis in der Ecke – Grün = 33 (Quadrat 9, Kreis durch die Ecke, berührt die Gegenseite)."""
from gemeinsam import *  # noqa: F401,F403
from shapely.geometry import Polygon as SP, Point as SPt

s = 9.0
A, B, C, D = P(0, 0), P(s, 0), P(s, s), P(0, s)
M, r = P(4, 3), 5.0
Pp, Q, T, A2 = P(8, 0), P(0, 6), P(9, 3), P(8, 6)
QUADRAT = SP([A, B, C, D])
KREIS = SPt(M).buffer(r, 2048)
GRUEN_FL = QUADRAT.symmetric_difference(KREIS)
GRUEN_D = "#1E8A45"


def grund(ax, gruen):
    form(ax, GRUEN_FL, gruen)
    for p, q in ((A, B), (B, C), (C, D), (D, A)):
        G.linie(ax, p, q)
    kreis(ax, M, r)
    for p in (A, Pp, Q, T):
        G.punkt(ax, p)


def frage(ax, sp):
    grund(ax, GRUEN)
    masslinie(ax, Pp, B, "1", -0.8, 26)
    masslinie(ax, Q, D, "3", 0.8, 26)
    G.text(ax, (7.6, 7.6), "?", 36)
    return D, C


def loesung(ax, sp):
    from shapely.geometry import box
    form(ax, GRUEN_FL, HGRUEN)
    for kappe in (KREIS.intersection(box(-2, -3, 10, 0)), KREIS.intersection(box(-2, -3, 0, 10))):
        form(ax, kappe, GRUEN)
    for kappe in (KREIS.intersection(box(-2, 6, 10, 10)), KREIS.intersection(box(8, -3, 10, 10))):
        for g in getattr(kappe, "geoms", [kappe]):
            ax.add_patch(Polygon(np.asarray(g.exterior.coords), closed=True, fc="none", ec=GRUEN_D, lw=0,
                                 hatch="///", zorder=3))
    for p, q in ((A, B), (B, C), (C, D), (D, A)):
        G.linie(ax, p, q)
    kreis(ax, M, r)
    strich(ax, Pp, A2, ROT, 2.4)
    strich(ax, A2, Q, ROT, 2.4)
    for p in (A, Pp, Q, T, M, A2):
        G.punkt(ax, p, 6)
    masslinie(ax, Pp, B, "1", -0.8, 22)
    masslinie(ax, Q, D, "3", 0.8, 22)
    G.text(ax, (4, 0.45), "8", 20, ROT)
    G.text(ax, (0.45, 4.5), "6", 20, ROT)
    G.text(ax, (2.3, 2.0), "48", 30, ROT)
    for von, nach, rad in (((5.2, -1.0), (5.2, 6.9), 0.35), ((-0.45, 1.8), (8.45, 1.8), -0.35)):
        ax.annotate("", xy=nach, xytext=von, arrowprops=dict(arrowstyle="-|>", color=GRUEN_D, lw=2.2,
                    mutation_scale=18, connectionstyle=f"arc3,rad={rad}"), zorder=9)
    return None


erzeuge(10,
        dict(DE=("Grün = ?", "Quadrat"), EN=("Green = ?", "square"), zeichne=frage),
        dict(DE=("Lösung: Grün = 81 − 48 = 33", "rechter Winkel an der Ecke: Rechteck 8 × 6 im Kreis; Stücke umlegen"),
             EN=("Solution: Green = 81 − 48 = 33", "right angle at the corner: 8 × 6 rectangle in the circle; swap the caps"),
             zeichne=loesung))
