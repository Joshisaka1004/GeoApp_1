"""GR 16: Das Herz am Fuß der Höhe – Rot : Blau = 1 : 2 (drei einbeschriebene Quadrate, rechtwinkliges Dreieck)."""
from gemeinsam import *  # noqa: F401,F403
from shapely.geometry import Polygon as SP
from shapely.ops import unary_union

a, b = 0.8 * 23.4, 23.4                 # Katheten BC, AC (Form 4 : 5: kein winziges Splitterstück)
c = math.hypot(a, b)
h = a * b / c
A, B = P(0, 0), P(c, 0)
H = P(b * b / c, 0)
C = P(b * b / c, a * b / c)
s = c * h / (c + h)
D = P(b * s / a, 0)
E, F, Gq = D + P(s, 0), D + P(s, s), D + P(0, s)
QS = [D, E, F, Gq]


def aehnlich(p_alt, p_neu):
    """Affine (hier: Ähnlichkeits-)Abbildung, die drei Punkte auf drei Punkte schickt."""
    M = np.array([[x[0], x[1], 1] for x in p_alt])
    return lambda z: np.linalg.solve(M, np.array(p_neu)).T @ np.array([z[0], z[1], 1])


f1 = aehnlich([A, B, C], [A, C, H])     # großes Dreieck → linkes Teildreieck
f2 = aehnlich([A, B, C], [C, B, H])     # großes Dreieck → rechtes Teildreieck
S1 = [f1(z) for z in QS]
S2 = [f2(z) for z in QS]
X = S1[2]                               # gemeinsame Ecke auf der Höhe (= S2[3])
ROT_FL = SP([D, X, E])
BLAU_FL = unary_union([SP(S1), SP(S2)]).difference(SP(QS))


def grund(ax, rot, blau):
    G.flaeche(ax, [A, B, C], "white")
    form(ax, BLAU_FL, blau)
    G.flaeche(ax, [D, X, E], rot, rand=False)
    for q in (QS, S1, S2):
        for i in range(4):
            G.linie(ax, q[i], q[(i + 1) % 4], lw=1.8)
    for p, q in ((A, B), (B, C), (C, A)):
        G.linie(ax, p, q)
    G.linie(ax, C, H, lw=1.8)
    G.rechter_winkel(ax, C, A, B, 1.1)
    G.rechter_winkel(ax, H, A, C, 1.0)
    G.rechter_winkel(ax, F, E, Gq, 0.9)                 # Kästchen zeigen die drei Quadrate
    G.rechter_winkel(ax, S1[0], S1[1], S1[3], 0.9)
    G.rechter_winkel(ax, S2[1], S2[0], S2[2], 0.9)
    for p in [Gq, F, X, D, E] + [S1[0], S1[1], S2[0], S2[1]]:
        G.punkt(ax, p, 6)


def frage(ax, sp):
    grund(ax, ROT, BLAU)
    return A, P(c * 0.45, 0)


def loesung(ax, sp):
    grund(ax, HROT, HBLAU)
    m = (D + F) / 2
    dreh = lambda z: m + np.array([[0, -1], [1, 0]]) @ (np.asarray(z) - m)     # Vierteldrehung um die Quadratmitte
    Z = D + (X - D) * ((E[0] - D[0]) / (X[0] - D[0]))                          # Gerade D–X trifft die rechte Seite
    Y = E + (X - E) * ((F[1] - E[1]) / (X[1] - E[1]))                          # Gerade E–X trifft die Oberseite
    X2 = dreh(X)                                                               # Spitze des gedrehten Dreiecks
    form(ax, SP([X, Z, F, Y]), GELB, z=3)                                      # die freie weiße Restfläche
    G.flaeche(ax, [D, X, E], ROT, rand=False)
    ax.add_patch(Polygon([E, X2, F], closed=True, fc="none", ec=ROT, lw=2.4, ls="--", zorder=7))
    ax.add_patch(Polygon([E, X, Z], closed=True, fc="none", ec=ROT, lw=0, hatch="///", zorder=6))
    ax.add_patch(Polygon([F, X2, Y], closed=True, fc="none", ec=ROT, lw=2.4, ls=":", zorder=7))
    for q in (QS, S1, S2):
        for i in range(4):
            G.linie(ax, q[i], q[(i + 1) % 4], lw=1.8)
    G.linie(ax, D, X, lw=2.6)
    G.linie(ax, X, E, lw=2.6)
    G.punkt(ax, m, 5)
    pfeil = dict(arrowstyle="-|>", color=ROT, lw=2, connectionstyle="arc3,rad=0.4", mutation_scale=16)
    ax.annotate("", xy=dreh(m + P(2.2, 0)), xytext=m + P(2.2, 0), arrowprops=pfeil, zorder=9)
    s1, s2 = (E + X + Z) / 3, (F + X2 + Y) / 3
    ax.annotate("", xy=s2, xytext=s1, arrowprops=dict(pfeil, connectionstyle="arc3,rad=-0.35"), zorder=9)
    G.text(ax, (D + X + E) / 3 + P(0, -0.3), "1", 20, "white")
    G.text(ax, s1 + P(0.55, -0.35), "2", 20, ROT)
    return None


erzeuge(16,
        dict(DE=("Rot : Blau = ?", "drei Quadrate"), EN=("Red : Blue = ?", "three squares"), zeichne=frage),
        dict(DE=("Lösung: Rot : Blau = 1 : 2",
                 "kleine Quadrate zusammen = großes, also Blau = Gelb + Rot\n"
                 "Rot 1 um 90° um die Quadratmitte drehen; das schraffierte Stück 2\n"
                 "ragt ins rechte Quadrat, um weitere 90° gedreht füllt es die Lücke:  Gelb = Rot"),
             EN=("Solution: Red : Blue = 1 : 2",
                 "small squares together = big one, so Blue = Yellow + Red\n"
                 "turn Red 1 by 90° about the square's centre; the hatched piece 2\n"
                 "sticks into the right square; turned another 90° it fills the gap:  Yellow = Red"),
             zeichne=loesung))
