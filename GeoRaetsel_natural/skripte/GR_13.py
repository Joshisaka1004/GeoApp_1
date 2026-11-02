"""GR 13: Die Pagode – 5/6 gefärbt (Turm aus Quadraten, Ketten aus Quadraten, Zahn = Quadrat)."""
from gemeinsam import *  # noqa: F401,F403
from matplotlib.patches import Rectangle

A, B, S = P(-2, 0), P(2, 0), P(0, 4)
STUFEN = 9


def quadrate():
    """Liste (x0, y0, seite) aller Quadrate und Liste der Zähne (Dreiecke), rechts und links."""
    qs, zaehne = [], []
    for k in range(STUFEN):
        s = 2 / 2 ** k
        y = 4 - 4 / 2 ** k
        qs.append((-s / 2, y, s))
        for j in range(1, 12):
            d = s / 3 ** j
            if d < 0.004:
                break
            innen = s * (1 - 3 ** (1 - j) / 2)
            for sg in (1, -1):
                x0 = innen if sg > 0 else -innen - d
                qs.append((x0, y, d))
                xi, xa = sg * innen, sg * (innen + d)
                zaehne.append([P(xi, y + d), P(xa, y + d), P(xi, y + 3 * d)])
    return qs, zaehne


QS, ZAEHNE = quadrate()


def grund(ax, farbe, lw_q=1.2):
    G.flaeche(ax, [A, B, S], "white")
    for x0, y0, s in QS:
        ax.add_patch(Rectangle((x0, y0), s, s, fc=farbe, ec=G.INK, lw=lw_q if s > 0.05 else 0.5, zorder=3))
    for p, q in ((A, B), (B, S), (S, A)):
        G.linie(ax, p, q)
    for p, q in ((A, P(-1, 0)), (P(-1, 0), P(0, 0)), (P(0, 0), P(1, 0)), (P(1, 0), B)):
        G.gleich(ax, p, q, 1, laenge=0.16)
    for p in (A, B, S, P(-1, 0), P(0, 0), P(1, 0), P(-1, 2), P(1, 2)):
        G.punkt(ax, p, 6)


def frage(ax, sp):
    grund(ax, ORANGE)
    return A, S


def loesung(ax, sp):
    grund(ax, "#F9D3B0", 0.9)
    strich(ax, P(-1, 2), P(1, 2), BLAU, 2.4)
    strich(ax, P(-1, 0), P(-1, 2), BLAU, 2.4)
    ax.add_patch(Polygon([P(-2, 0), P(-1, 0), P(-1, 2)], closed=True, fc="none", ec=BLAU, lw=0, hatch="///",
                         zorder=4))
    # Zahn über dem ersten rechten Kettenquadrat: Spitze abschneiden und umklappen → Quadrat
    G.flaeche(ax, [P(1, 2 / 3), P(5 / 3, 2 / 3), P(1, 2)], "white", rand=False)
    strich(ax, P(1, 4 / 3), P(4 / 3, 4 / 3), ROT, 2.2)
    ax.add_patch(Polygon([P(4 / 3, 4 / 3), P(5 / 3, 4 / 3), P(5 / 3, 2 / 3)], closed=True, fc="none", ec=ROT,
                         lw=2, ls="--", zorder=6))
    ax.annotate("", xy=(1.55, 1.2), xytext=(1.12, 1.75), arrowprops=dict(arrowstyle="-|>", color=ROT, lw=2,
                connectionstyle="arc3,rad=-0.5", mutation_scale=16), zorder=9)
    return None


erzeuge(13,
        dict(DE=("Welcher Anteil ist gefärbt?", "Quadrate; Turm und Seitenketten gehen endlos weiter"),
             EN=("What fraction is shaded?", "squares; tower and side chains go on forever"), zeichne=frage),
        dict(DE=("Lösung: 5/6 gefärbt", "Ecken = 1/3 jeder Stufe;  jeder weiße Zahn = Quadrat darunter → 1/6 weiß"),
             EN=("Solution: 5/6 shaded", "corners = 1/3 of each level;  each white tooth = the square below → 1/6 white"),
             zeichne=loesung))
