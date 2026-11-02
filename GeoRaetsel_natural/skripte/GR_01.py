"""GR 01: Strahlen aus der kleinen Ecke – Blau = 73 (drei Quadrate 14, 10, 7,5)."""
from gemeinsam import *  # noqa: F401,F403

a, b = 14.0, 10.0
c = b * (2 * b - a) / (2 * (a - b))          # 7,5 – folgt aus „R ist Mitte von P2Q2“
O, A, B, C = P(0, 0), P(a, 0), P(a + b, 0), P(a + b + c, 0)
P1, Q1, P2, Q2, P3, Q3 = P(0, a), P(a, a), P(a, b), P(a + b, b), P(a + b, c), P(a + b + c, c)
R = P(a + b / 2, b)
X1 = P(a, a * (b + c) / (a + b + c))
Y1 = P(a + b, a * c / (a + b + c))
Y2 = P(a + b, b * c / (b + c))


def quadrate(ax):
    for q in ([O, A, Q1, P1], [A, B, Q2, P2], [B, C, Q3, P3]):
        for i in range(4):
            G.linie(ax, q[i], q[(i + 1) % 4])


def frage(ax, sp):
    for poly in ([P1, Q1, X1], [X1, P2, Y2, Y1], [Y1, Y2, C], [P2, Q1, R]):
        G.flaeche(ax, poly, BLAU, rand=False)
    quadrate(ax)
    for p in (P1, Q1, P2):
        G.linie(ax, C, p)
    G.gleich(ax, P2, R, 1, laenge=0.9)
    G.gleich(ax, R, Q2, 1, laenge=0.9)
    for p in (O, A, B, C, P1, Q1, P2, Q2, P3, Q3, R):
        G.punkt(ax, p)
    G.mass(ax, O, P1, "14", 1.3)
    masslinie(ax, A, B, "10", -1.3, 28)
    return O, A


def loesung(ax, sp):
    G.flaeche(ax, [O, Q1, P1], HBLAU, rand=False)
    G.flaeche(ax, [A, R, P2], HROT, rand=False)
    quadrate(ax)
    for p in (P1, Q1, P2):
        G.linie(ax, C, p, lw=1.8)
    strich(ax, O, Q1, BLAU, 2.4)
    strich(ax, A, R, ROT, 2.4)
    G.gleich(ax, P2, R, 1, laenge=0.9)
    G.gleich(ax, R, Q2, 1, laenge=0.9)
    for p in (O, A, C, P1, Q1, P2, R):
        G.punkt(ax, p)
    G.text(ax, (4.2, 9.6), "98", 30, BLAU)
    G.text(ax, (15.05, 4.6), "25", 24, ROT)
    G.mass(ax, O, P1, "14", 1.3)
    ax.annotate("", xy=(0.6, -1.3), xytext=(30.9, -1.3),
                arrowprops=dict(arrowstyle="-|>", color=BLAU, lw=2.2, mutation_scale=22))
    ax.annotate("", xy=(14.6, -2.6), xytext=(30.9, -2.6),
                arrowprops=dict(arrowstyle="-|>", color=ROT, lw=2.2, mutation_scale=22))
    return None


erzeuge(1,
        dict(DE=("Blau = ?", "drei Quadrate"), EN=("Blue = ?", "three squares"), zeichne=frage),
        dict(DE=("Lösung: Blau = 98 − 25 = 73", "Spitze auf dem Boden verschieben: Fläche bleibt gleich"),
             EN=("Solution: Blue = 98 − 25 = 73", "slide the apex along the ground: the area stays the same"),
             zeichne=loesung))
