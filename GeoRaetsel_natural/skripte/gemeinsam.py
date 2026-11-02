"""Gemeinsame Helfer für die Karten GR_01 … GR_10 (GeoRätsel natural, 01.11.2026).

Jedes Skript GR_XX.py ruft `erzeuge(nr, frage, loesung)` auf:
  frage   = dict(DE=(titel, unterschrift), EN=(...), zeichne=f(ax, sprache))
  loesung = dict(DE=(titel, unterschrift), EN=(...), zeichne=f(ax, sprache))
Es entstehen GR_XX_DE.png, GR_XX_EN.png, GR_XX_Loesung_DE.png, GR_XX_Loesung_EN.png im Ausgabeordner.
"""
import math
import os
import sys

HIER = os.path.dirname(os.path.abspath(__file__))
AUSGABE = os.path.dirname(HIER)
sys.path.insert(0, os.path.join(os.path.dirname(AUSGABE), "Werkzeug_natural"))

import numpy as np  # noqa: E402
import georaetsel_natural as G  # noqa: E402
from matplotlib.patches import Polygon, Circle, FancyBboxPatch  # noqa: E402

DATUM = "01.11.2026"
ROT, BLAU, GRUEN, GELB, ORANGE = "#D62F3F", "#3B82D6", "#4CC46A", "#FDE28A", "#F2994A"
HROT, HBLAU, HGRUEN, HGELB, GRAU = "#F7C6CB", "#CFE3FA", "#CDEFD5", "#FFF5CC", "#777777"


def erzeuge(nr, frage, loesung=None):
    for sp in ("DE", "EN"):
        t, u = frage[sp]
        G.karte(nr, DATUM, sp, t, u, frage["zeichne"], os.path.join(AUSGABE, f"GR_{nr:02d}_{sp}.png"))
        if loesung:
            t, u = loesung[sp]
            G.karte(nr, DATUM, sp, t, u, loesung["zeichne"],
                    os.path.join(AUSGABE, f"GR_{nr:02d}_Loesung_{sp}.png"))
    print("fertig: GR_%02d" % nr)


def P(x, y):
    return np.array([x, y], float)


def strich(ax, p, q, farbe=GRAU, lw=2.0):
    """Gestrichelte Hilfslinie (nur Lösungsbild)."""
    G.linie(ax, p, q, lw=lw, farbe=farbe, linestyle=(0, (6, 4)))


def kreis(ax, m, r, lw=G.LW, fc="none", z=4, farbe=G.INK, **kw):
    ax.add_patch(Circle(m, r, fc=fc, ec=farbe, lw=lw, zorder=z, **kw))


def bogenpunkte(m, r, a1, a2, n=200):
    """Punkte auf dem Kreisbogen um m von Winkel a1 bis a2 (Grad, gegen den Uhrzeiger)."""
    t = np.radians(np.linspace(a1, a2, n))
    return [m + r * np.array([math.cos(u), math.sin(u)]) for u in t]


def form(ax, geom, farbe, rand=False, z=2):
    """Shapely-Fläche (auch MultiPolygon) füllen."""
    geoms = getattr(geom, "geoms", [geom])
    for g in geoms:
        if g.is_empty or g.area < 1e-9:
            continue
        ax.add_patch(Polygon(np.asarray(g.exterior.coords), closed=True, fc=farbe,
                             ec=G.INK if rand else "none", lw=G.LW if rand else 0, zorder=z))


def rahmen(ax, mitte, breite, hoehe, farbe=ROT):
    """Abgerundeter Rahmen für die Formel einer Beweisaufgabe."""
    x, y = mitte[0] - breite / 2, mitte[1] - hoehe / 2
    ax.add_patch(FancyBboxPatch((x, y), breite, hoehe, boxstyle="round,pad=0.02,rounding_size=0.5",
                                fc="white", ec=farbe, lw=3, zorder=8))


def schrift(ax, p, t, groesse=26, farbe=G.INK, **kw):
    ax.text(p[0], p[1], t, ha="center", va="center", fontsize=groesse, fontweight="bold", color=farbe,
            zorder=26, **kw)


def masslinie(ax, p, q, t, versatz, groesse=28, farbe=G.INK, lw=1.5, ende=0.35, anteil=0.5):
    """Maßlinie parallel zu p–q (versetzt nach links von p→q) mit Endstrichen und Zahl in der Mitte."""
    p, q = np.asarray(p, float), np.asarray(q, float)
    d = (q - p) / np.linalg.norm(q - p)
    n = np.array([-d[1], d[0]])
    a, b = p + n * versatz, q + n * versatz
    G.linie(ax, p + n * 0.25 * np.sign(versatz), a + n * 0.3 * np.sign(versatz), lw=1.0, farbe=farbe)
    G.linie(ax, q + n * 0.25 * np.sign(versatz), b + n * 0.3 * np.sign(versatz), lw=1.0, farbe=farbe)
    ax.annotate("", xy=b, xytext=a, arrowprops=dict(arrowstyle="<|-|>", color=farbe, lw=lw,
                                                    mutation_scale=16, shrinkA=0, shrinkB=0), zorder=7)
    m = a + anteil * (b - a)
    ax.text(m[0], m[1], t, ha="center", va="center", fontsize=groesse, fontweight="bold", color=farbe, zorder=26,
            bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none"))


def farbformel(fig, y_px, teile, groesse=40, rahmenfarbe=ROT):
    """Formel aus farbigen Teilen [(text, farbe), …] mittig auf der Karte, y_px von oben, in einem Rahmen."""
    r = fig.canvas.get_renderer()
    breiten = []
    for t, f in teile:
        h = fig.text(0, 0, t, fontsize=groesse, fontweight="bold")
        breiten.append(h.get_window_extent(r).width)
        h.remove()
    gesamt = sum(breiten)
    x = 550 - gesamt / 2
    y = 1 - y_px / 1100
    for (t, f), b in zip(teile, breiten):
        fig.text(x / 1100, y, t, fontsize=groesse, fontweight="bold", color=f, va="center", ha="left")
        x += b
    w, hgt = gesamt + 70, groesse * 2.0
    fig.patches.append(FancyBboxPatch(((550 - w / 2) / 1100, y - hgt / 2 / 1100), w / 1100, hgt / 1100,
                                      boxstyle="round,pad=0.004,rounding_size=0.02", fc="none", ec=rahmenfarbe,
                                      lw=3, transform=fig.transFigure, figure=fig))


def gleich_bei(ax, p, q, f, n=1, laenge=0.45):
    """Gleichheitsstriche wie G.gleich, aber an der Stelle f (0…1) der Strecke p–q statt in der Mitte."""
    p, q = np.asarray(p, float), np.asarray(q, float)
    c = p + f * (q - p)
    u = (q - p) / np.linalg.norm(q - p) * 0.3
    G.gleich(ax, c - u, c + u, n, laenge=laenge)
