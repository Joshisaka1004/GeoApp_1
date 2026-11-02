"""GR 03: Das leere Viertel – Anteil = 1/2 (zwei senkrechte Sehnen, zwei Achtelkreise, zwei Halbkreise)."""
from gemeinsam import *  # noqa: F401,F403
from shapely.geometry import Polygon as SP, Point as SPt

O = P(0, 0)
RK = 5.0
WURZEL = math.sqrt(0.5)


def _ecke_auf_kreis(q, p):
    """Abstand der 45°-Ecke des großen Achtelkreises von der Mitte minus Radius (soll 0 sein)."""
    pa = math.sqrt(RK * RK - q * q) - p
    return math.hypot(p + pa * WURZEL, q + pa * WURZEL) - RK


# Kreuzungspunkt so, dass die Ecke des großen Achtelkreises genau auf dem Kreis liegt
from scipy.optimize import brentq  # noqa: E402
_p = -3.1
_q = brentq(_ecke_auf_kreis, -1.6, -1.0, args=(_p,))
Pp = P(_p, _q)
_a, _b = math.sqrt(RK * RK - _q * _q), math.sqrt(RK * RK - _p * _p)
A, B, C, D = P(_a, _q), P(_p, _b), P(-_a, _q), P(_p, -_b)
PA, PB, PC, PD = _a - _p, _b - _q, _a + _p, _b + _q
E1 = Pp + PA * P(WURZEL, WURZEL)
F1 = Pp + PB * P(WURZEL, WURZEL)

STUECKE = [
    [Pp] + bogenpunkte(Pp, PA, 0, 45),
    [Pp] + bogenpunkte(Pp, PB, 45, 90),
    bogenpunkte(Pp - P(PC / 2, 0), PC / 2, 0, 180),
    bogenpunkte(Pp - P(0, PD / 2), PD / 2, -90, 90),
]


def grund(ax, farbe):
    kreis(ax, O, RK, fc="white", z=1)
    for s in STUECKE:
        G.flaeche(ax, s, farbe)
    G.linie(ax, C, A, lw=2)
    G.linie(ax, D, B, lw=2)
    G.rechter_winkel(ax, Pp, C, D, 0.42)
    for p in (Pp, A, B, C, D, E1):
        G.punkt(ax, p)


def frage(ax, sp):
    grund(ax, BLAU)
    return 5 * P(math.cos(math.radians(-68)), math.sin(math.radians(-68))), 5 * P(math.cos(math.radians(-38)), math.sin(math.radians(-38)))


def loesung(ax, sp):
    grund(ax, HBLAU)
    strich(ax, A, B, ROT)
    strich(ax, C, D, ROT)
    G.text(ax, (1.0, -1.95), "a", 24)
    G.text(ax, (-2.6, 0.3), "b", 24)
    G.text(ax, (-3.95, -0.1), "c", 20)
    G.text(ax, (-3.48, -2.6), "d", 18)
    G.text(ax, (2.3, -0.5), "π/8 · a²", 20, BLAU)
    G.text(ax, (-1.3, 2.25), "π/8 · b²", 17, BLAU)
    return None


erzeuge(3,
        dict(DE=("Welcher Anteil ist gefärbt?", "zwei Achtelkreise, zwei Halbkreise"),
             EN=("What fraction is shaded?", "two eighth circles, two semicircles"), zeichne=frage),
        dict(DE=("Lösung: genau die Hälfte", "jedes Stück = π/8 · Stück²;  a² + b² + c² + d² = Durchmesser²"),
             EN=("Solution: exactly one half", "each piece = π/8 · length²;  a² + b² + c² + d² = diameter²"),
             zeichne=loesung))
