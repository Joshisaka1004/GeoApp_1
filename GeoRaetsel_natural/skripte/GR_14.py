"""GR 14: Das Zelt über der Seite – x = 25° (PB = PC = CA, 2x bei A, 4x bei P, Außenwinkel 6x bei B)."""
from gemeinsam import *  # noqa: F401,F403

d = math.radians
B = P(0, 0)
C = P(10 * math.sin(d(50)), 0)
A = 10 * math.sin(d(100)) * P(math.cos(d(30)), math.sin(d(30)))
Pp = P(5 * math.sin(d(50)), 5 * math.cos(d(50)))
E = B - 0.32 * (A - B)


def _schnitt(p1, p2, p3, p4):
    d1, d2 = p2 - p1, p4 - p3
    return p1 + np.cross(p3 - p1, d2) / np.cross(d1, d2) * d1


Q = _schnitt(Pp, C, A, B)                # Zeltstange kreuzt die Seite AB
GRUEN_D = "#2E9E57"


def grund(ax, hell=False):
    for p, q in ((A, B), (B, C), (C, A), (Pp, B), (Pp, C), (B, E)):
        G.linie(ax, p, q)
    for p, q in ((Pp, B), (Pp, C), (C, A)):
        G.gleich(ax, p, q, 1, laenge=0.4)
    G.winkel(ax, A, B, C, 2.3, "2x", HGRUEN if hell else "#9FE0B0", abstand=0.72, groesse=20)
    G.winkel(ax, Pp, B, C, 0.78, "4x", HBLAU if hell else "#9CC8F2", abstand=0.6, groesse=15)
    G.winkel(ax, B, C, E, 1.05, "6x", "#FCD9B8" if hell else "#F7B57C", abstand=0.66, groesse=20)
    for p in (A, B, C, Pp):
        G.punkt(ax, p)


def frage(ax, sp):
    grund(ax)
    return E, B


def loesung(ax, sp):
    G.flaeche(ax, [A, Pp, C], HGELB, rand=False)
    grund(ax, hell=True)
    kreis(ax, Pp, 5.0, lw=1.6, farbe=GRAU, linestyle=(0, (6, 4)))
    G.linie(ax, Pp, A, lw=2.2, farbe=ROT)
    G.gleich(ax, Pp, A, 1, laenge=0.4)
    G.text(ax, Pp + P(1.55, 0.25), "60°", 16, ROT)
    G.winkel(ax, B, C, A, 3.3, "30°", None, abstand=0.84, groesse=15)
    return None


erzeuge(14,
        dict(DE=("x = ?", ""), EN=("x = ?", ""), zeichne=frage),
        dict(DE=("Lösung: 6x = 150°, x = 25°", "Zeltspitze = Mitte des Kreises durch die Ecken; gelb gleichseitig → 30° bei B"),
             EN=("Solution: 6x = 150°, x = 25°", "tent tip = centre of the circle through the corners; yellow equilateral → 30° at B"),
             zeichne=loesung))
