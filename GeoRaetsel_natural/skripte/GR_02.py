"""GR 02: Der Abstand zur langen Seite – x = 6° (PA = PB = BC, Winkel 3x/4x bei B, 3x/2x bei A)."""
from gemeinsam import *  # noqa: F401,F403

d = math.radians
B = P(0, 0)
A = P(20 * math.cos(d(18)), 0)
C = 10 * P(math.cos(d(42)), math.sin(d(42)))
Pp = 10 * P(math.cos(d(18)), math.sin(d(18)))
M = (Pp + C) / 2
u = (C - A) / np.linalg.norm(C - A)
H = A + u * np.dot(Pp - A, u)


def grund(ax, voll=True):
    for p, q in ((A, B), (B, C), (C, A), (Pp, A), (Pp, B)):
        G.linie(ax, p, q)
    G.gleich(ax, Pp, A, 2, laenge=0.7)
    G.gleich(ax, B, C, 2, laenge=0.7)
    G.winkel(ax, B, A, Pp, 4.4, "3x", HGRUEN, abstand=0.74, groesse=22)
    G.winkel(ax, B, Pp, C, 3.6, "4x", "#FCD9B8", abstand=0.6, groesse=20)
    G.winkel(ax, A, B, Pp, 4.4, "3x", HGRUEN, abstand=0.74, groesse=22)
    G.winkel(ax, A, Pp, C, 8.6, "2x", BLAU if voll else HBLAU, abstand=0.86, groesse=24)
    for p in (A, B, C, Pp):
        G.punkt(ax, p)


def frage(ax, sp):
    grund(ax)
    return C, A


def loesung(ax, sp):
    G.flaeche(ax, [Pp, B, M], HGELB, rand=False)
    G.flaeche(ax, [Pp, A, H], HGELB, rand=False)
    grund(ax, voll=False)
    strich(ax, Pp, C, G.INK)
    strich(ax, B, M, ROT)
    strich(ax, Pp, H, ROT)
    G.rechter_winkel(ax, M, B, C, 0.45)
    G.rechter_winkel(ax, H, Pp, C, 0.45)
    G.gleich(ax, Pp, M, 1, laenge=0.5)
    G.gleich(ax, M, C, 1, laenge=0.5)
    G.winkel(ax, C, Pp, A, 2.9, "30°", "#FCD9B8", abstand=0.76, groesse=18)
    for p in (M, H):
        G.punkt(ax, p, 5)
    return None


erzeuge(2,
        dict(DE=("x = ?", ""), EN=("x = ?", ""), zeichne=frage),
        dict(DE=("Lösung: x = 6°", "gleiche gelbe Dreiecke: Abstand = halbe Strecke, also 30°"),
             EN=("Solution: x = 6°", "equal yellow triangles: distance = half the segment, so 30°"),
             zeichne=loesung))
