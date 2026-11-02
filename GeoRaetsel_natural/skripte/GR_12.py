"""GR 12: Der Giebel über drei Quadraten – x = 13 (Giebellinien 22 und 19, 22² + 19² = 5 · x²)."""
from gemeinsam import *  # noqa: F401,F403

a, b = math.sqrt(105), 8.0
O = P(0, 0)
Q, L1 = P(a, a), P(0, a)
Pp = P(a + b, 0)
R = P(2 * a, a + b)
S = P(2 * a + b, b)
L2 = P(2 * a + 2 * b, b)
H1, H2 = P(2 * a, a), P(2 * a, b)


def grund(ax, x_farbe):
    G.linie(ax, P(-1.5, 0), P(2 * a + 2 * b + 1.5, 0))
    G.flaeche(ax, [Pp, S, R, Q], "#F4F4F4")
    for poly in ([O, P(a, 0), Q, L1], [P(2 * a + b, 0), P(2 * a + 2 * b, 0), L2, S]):
        G.flaeche(ax, poly, "white")
    G.linie(ax, L1, R)
    G.linie(ax, R, L2)
    G.linie(ax, Pp, Q, lw=6, farbe=x_farbe)
    for p in (Pp, Q, S, R, L1, L2):
        G.punkt(ax, p)
    masslinie(ax, L1, R, "22", 1.6, 28)
    masslinie(ax, R, L2, "19", 1.6, 28)
    G.text(ax, (a + b / 2 - 1.5, a / 2 - 0.6), "x", 32, x_farbe)


def frage(ax, sp):
    grund(ax, ROT)
    return P(2 * a + 2 * b - 7, 0), P(2 * a + 2 * b, 0)


def loesung(ax, sp):
    grund(ax, ROT)
    for poly in ([P(a, 0), Pp, Q], [Pp, P(2 * a + b, 0), S], [Q, H1, R], [R, H2, S]):
        G.flaeche(ax, poly, HGELB, rand=False)
    for p, q in ((Q, R), (R, S), (S, Pp), (P(a, 0), Q), (S, P(2 * a + b, 0))):
        G.linie(ax, p, q)
    G.text(ax, (a + b / 2, -1.0), "b", 22)
    G.text(ax, (a + b + a / 2, -1.0), "a", 22)
    strich(ax, Q, H1, BLAU, 2.4)
    strich(ax, H1, R, BLAU, 2.4)
    strich(ax, R, H2, GRUEN, 2.4)
    strich(ax, H2, S, GRUEN, 2.4)
    G.text(ax, (a / 2, a + 0.0 - 1.0), "a", 22, BLAU)
    G.text(ax, ((a + 2 * a) / 2, a - 1.0), "a", 22, BLAU)
    G.text(ax, (2 * a + 0.9, a + b / 2), "b", 22, BLAU)
    G.text(ax, (2 * a - 0.9, (a + b + b) / 2 + 2.6), "a", 22, GRUEN)
    G.text(ax, (2 * a + b / 2, b - 1.0), "b", 22, GRUEN)
    G.text(ax, (2 * a + 1.5 * b, b - 1.0), "b", 22, GRUEN)
    return None


erzeuge(12,
        dict(DE=("x = ?", "drei Quadrate"), EN=("x = ?", "three squares"), zeichne=frage),
        dict(DE=("Lösung: x = 13", "22² = 4a² + b²,  19² = a² + 4b²,  zusammen 845 = 5 · (a² + b²) = 5 · x²"),
             EN=("Solution: x = 13", "22² = 4a² + b²,  19² = a² + 4b²,  together 845 = 5 · (a² + b²) = 5 · x²"),
             zeichne=loesung))
