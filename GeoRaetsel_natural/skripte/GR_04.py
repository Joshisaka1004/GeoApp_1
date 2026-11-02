"""GR 04: Das versteckte Windrad – Gesamtfläche = 60 (regelmäßiges Achteck, gelbes Dreieck 5 = 1/12)."""
from gemeinsam import *  # noqa: F401,F403

s = 4.0
r = s * (1 + math.sqrt(2)) / 2
V = [P(-s / 2, -r), P(s / 2, -r), P(r, -s / 2), P(r, s / 2), P(s / 2, r), P(-s / 2, r), P(-r, s / 2), P(-r, -s / 2)]
Mi = [(V[i] + V[(i + 1) % 8]) / 2 for i in range(8)]          # Mitte der Seite V_i V_(i+1)


def schnitt(p1, p2, p3, p4):
    d1, d2 = p2 - p1, p4 - p3
    t = np.cross(p3 - p1, d2) / np.cross(d1, d2)
    return p1 + t * d1


SPEICHE = [(V[i], Mi[(i + 2) % 8]) for i in range(8)]
X = [schnitt(*SPEICHE[i], *SPEICHE[(i + 1) % 8]) for i in range(8)]


def umriss(ax):
    for i in range(8):
        G.linie(ax, V[i], V[(i + 1) % 8])


def frage(ax, sp):
    G.flaeche(ax, [V[0], V[1], X[0]], GELB, rand=False)
    umriss(ax)
    G.linie(ax, V[0], Mi[2])
    G.linie(ax, V[1], Mi[3])
    for p, q in ((V[2], Mi[2]), (Mi[2], V[3]), (V[3], Mi[3]), (Mi[3], V[4])):
        G.gleich(ax, p, q, 1, laenge=0.45)
    for p in (V[0], V[1], Mi[2], Mi[3]):
        G.punkt(ax, p)
    G.text(ax, (V[0] + V[1] + X[0]) / 3 + P(0, -0.05), "5", 34)
    return V[7], V[6]


def loesung(ax, sp):
    G.flaeche(ax, X, HBLAU, rand=False)
    for i in range(8):
        G.flaeche(ax, [V[i], V[(i + 1) % 8], X[i]], HGELB, rand=False)
        G.text(ax, (V[i] + V[(i + 1) % 8] + X[i]) / 3, "5", 22)
    umriss(ax)
    for i in range(8):                       # Speiche nur bis zur fernen Ecke des Innen-Achtecks
        p = V[i]
        q = max((X[i], X[i - 1]), key=lambda x: np.linalg.norm(x - p))
        if i in (0, 1):
            G.linie(ax, p, q)
        else:
            strich(ax, p, q, G.INK, 1.8)
    G.text(ax, (0, 0), "20", 34, BLAU)
    return None


erzeuge(4,
        dict(DE=("Gesamtfläche = ?", "regelmäßiges Achteck"), EN=("Total area = ?", "regular octagon"),
             zeichne=frage),
        dict(DE=("Lösung: Gesamtfläche = 60", "Windrad ergänzen: innen 1/3 = 20, außen 8 · 5 = 40"),
             EN=("Solution: total area = 60", "complete the pinwheel: inside 1/3 = 20, outside 8 · 5 = 40"),
             zeichne=loesung))
