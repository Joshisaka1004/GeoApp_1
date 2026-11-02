"""Hausstil der klassischen GeoRätsel (/geo-aufgaben-natural), wie Jochens Karte 27.10.2026 #04.

Karte 1100 × 1100 px, weiß. Oben fett die Frage als Titel, links senkrecht Datum und Nummer, unten eine kurze
kursive Bildunterschrift, die Signatur klein entlang einer Linie der Figur. Kein Aufgabentext: alles steht im Bild.

    import georaetsel_natural as G
    def zeichne(ax, sprache):            # ax in Rechenkoordinaten (y nach oben, gleiche Maßstäbe)
        G.linie(ax, (0, 0), (6, 0)); G.punkt(ax, (6, 0)); ...
        return (2, 0), (6, 0)              # Linie für die Signatur (oder None)
    G.karte(4, "01.11.2026", "DE", "Fläche = ?", "regelmäßiges Sechseck", zeichne, "GR_04_DE.png")

Probe:  python3 georaetsel_natural.py <zielordner>
"""
import math
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon, Wedge, Arc

plt.rcParams["font.family"] = "Arial"          # Inter ist auf dem Mac nicht installiert

INK = "#111111"
GELB, HGELB, GRUEN, HBLAU, ORANGE, ROT = "#FDE28A", "#FFF5CC", "#5CD67A", "#BFDFFF", "#F2994A", "#D62F3F"
LW = 2.6


def karte(nr, datum, sprache, titel, unterschrift, zeichne, datei, rand=0.06):
    """Zeichnet eine Karte. `zeichne(ax, sprache)` malt die Figur und gibt die Signaturlinie (p, q) oder None zurück."""
    fig = plt.figure(figsize=(11, 11), dpi=100)
    fig.patch.set_facecolor("white")
    ax0 = fig.add_axes([0, 0, 1, 1])
    ax0.set_xlim(0, 1100)
    ax0.set_ylim(1100, 0)
    ax0.axis("off")
    ax0.text(550, 70, titel, ha="center", va="center", fontsize=34, fontweight="bold", color=INK)
    ax0.text(42, 550, f"{datum}  #{nr:02d}" if isinstance(nr, int) else f"{datum}  #{nr}", ha="center",
             va="center", rotation=90, fontsize=17, fontweight="bold", color=INK)
    unten = 1000 if unterschrift else 1050
    if unterschrift:
        ax0.text(550, 1040, unterschrift, ha="center", va="center", fontsize=21, style="italic", color="#222222")
    ax = fig.add_axes([110 / 1100, 1 - unten / 1100, 880 / 1100, (unten - 130) / 1100])
    ax.axis("off")
    sig = zeichne(ax, sprache)
    ax.set_aspect("equal", adjustable="datalim")
    ax.set_anchor("C")
    x0, x1 = ax.get_xlim()
    y0, y1 = ax.get_ylim()
    dx, dy = (x1 - x0) * rand, (y1 - y0) * rand
    ax.set_xlim(x0 - dx, x1 + dx)
    ax.set_ylim(y0 - dy, y1 + dy)
    if sig:
        signatur(ax, sig[0], sig[1], "#GeoRätsel" if sprache == "DE" else "#GeoPuzzle")
    fig.savefig(datei, dpi=100, facecolor="white")
    plt.close(fig)


def signatur(ax, p, q, text):
    """Kleine Signatur mittig entlang der Strecke p–q, knapp darüber, lesbar (nie kopfüber)."""
    p, q = np.asarray(p, float), np.asarray(q, float)
    if q[0] < p[0]:
        p, q = q, p
    d = q - p
    n = np.array([-d[1], d[0]]) / np.linalg.norm(d)
    m = (p + q) / 2 + n * 0.018 * max(np.ptp(ax.get_xlim()), np.ptp(ax.get_ylim()))
    ax.text(m[0], m[1], text, ha="center", va="center", fontsize=11, fontweight="bold", color=INK,
            rotation=math.degrees(math.atan2(d[1], d[0])), rotation_mode="anchor", zorder=30)


# ------------------------------------------------------------------ Bausteine
def linie(ax, p, q, lw=LW, farbe=INK, **kw):
    ax.plot([p[0], q[0]], [p[1], q[1]], color=farbe, lw=lw, solid_capstyle="round", zorder=5, **kw)


def flaeche(ax, punkte, farbe, rand=True):
    ax.add_patch(Polygon(punkte, closed=True, fc=farbe, ec=INK if rand else "none", lw=LW, zorder=2,
                         joinstyle="round"))


def punkt(ax, p, r=7):
    """Wichtiger Punkt: kleiner weißer Kreis mit schwarzem Rand (Punkt auf Seite, Ecke, Schnittpunkt)."""
    ax.plot(p[0], p[1], "o", ms=r * 1.4, mfc="white", mec=INK, mew=2, zorder=20)


def text(ax, p, t, groesse=30, farbe=INK, **kw):
    """Zahl oder Fragezeichen in einer Teilfläche bzw. an einer Seite."""
    ax.text(p[0], p[1], t, ha="center", va="center", fontsize=groesse, fontweight="bold", color=farbe, zorder=25, **kw)


def gleich(ax, p, q, n=1, laenge=None):
    """n kurze Querstriche in der Mitte von p–q: Strecken mit gleich vielen Strichen sind gleich lang."""
    p, q = np.asarray(p, float), np.asarray(q, float)
    d = (q - p) / np.linalg.norm(q - p)
    nn = np.array([-d[1], d[0]])
    L = laenge or 0.035 * np.linalg.norm(q - p) + 0.12
    m = (p + q) / 2
    for k in range(n):
        c = m + d * (k - (n - 1) / 2) * L * 0.45
        linie(ax, c - nn * L / 2, c + nn * L / 2, lw=2)


def rechter_winkel(ax, ecke, p, q, s=0.4):
    """Kästchen für einen rechten Winkel an `ecke` zwischen den Richtungen zu p und q."""
    e = np.asarray(ecke, float)
    u = (np.asarray(p, float) - e) / np.linalg.norm(np.asarray(p, float) - e) * s
    v = (np.asarray(q, float) - e) / np.linalg.norm(np.asarray(q, float) - e) * s
    ax.plot(*zip(e + u, e + u + v, e + v), color=INK, lw=1.8, zorder=6)


def winkel(ax, scheitel, p, q, r, beschriftung="", farbe=None, abstand=0.62, groesse=26, striche=0):
    """Winkelbogen am Scheitel zwischen den Strahlen zu p und q (der kleinere Winkel), optional gefüllt und beschriftet.

    Die Beschriftung steht im Winkel (abstand = Bruchteil des Radius); bei sehr spitzen Winkeln den Bogen größer machen.
    """
    s = np.asarray(scheitel, float)
    a1 = math.degrees(math.atan2(p[1] - s[1], p[0] - s[0]))
    a2 = math.degrees(math.atan2(q[1] - s[1], q[0] - s[0]))
    lo, hi = a1, a2
    if (hi - lo) % 360 > 180:
        lo, hi = hi, lo
    hi = lo + (hi - lo) % 360
    if farbe:
        ax.add_patch(Wedge(s, r, lo, hi, fc=farbe, ec="none", zorder=3))
    ax.add_patch(Arc(s, 2 * r, 2 * r, theta1=lo, theta2=hi, color=INK, lw=1.8, zorder=6))
    mid = math.radians((lo + hi) / 2)
    for k in range(striche):
        t = math.radians(lo + (hi - lo) * (k + 1) / (striche + 1))
        linie(ax, s + 0.8 * r * np.array([math.cos(t), math.sin(t)]), s + 1.2 * r * np.array([math.cos(t), math.sin(t)]), lw=1.8)
    if beschriftung:
        text(ax, s + abstand * r * np.array([math.cos(mid), math.sin(mid)]), beschriftung, groesse)


def mass(ax, p, q, t, versatz=0.6, groesse=30):
    """Längenangabe: Zahl mittig neben der Strecke, auf der Seite, zu der die Normale (links von p→q) zeigt."""
    p, q = np.asarray(p, float), np.asarray(q, float)
    d = (q - p) / np.linalg.norm(q - p)
    text(ax, (p + q) / 2 + np.array([-d[1], d[0]]) * versatz, t, groesse)


# ------------------------------------------------------------------ Probe
if __name__ == "__main__":
    ziel = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))

    def probe(ax, sprache):
        A, B, C, D = (0, 0), (8, 0), (8, 8), (0, 8)
        P = (8, 3)
        flaeche(ax, [A, B, C, D], "white")
        flaeche(ax, [A, B, P], GRUEN)
        linie(ax, A, P)
        linie(ax, P, D)
        for x in (A, B, C, D, P):
            punkt(ax, x)
        text(ax, (5.6, 1.1), "?", 34)
        mass(ax, D, C, "8", 0.6)
        mass(ax, B, P, "3", 0.55)
        rechter_winkel(ax, B, A, C)
        winkel(ax, D, P, A, 1.8, "x", ORANGE)
        return D, P

    for sp, t, u in (("DE", "Grün = ?", "Quadrat"), ("EN", "Green = ?", "square")):
        karte(0, "01.11.2026", sp, t, u, probe, os.path.join(ziel, f"Probe_{sp}.png"))
    print("Probe geschrieben nach", ziel)
