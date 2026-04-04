"""
Problème : 
    Dans un rectangle de longueur 4 et de largeur 3, 
    on peut dessiner 12 carrés de côté 1, 6 carrés de côté 2 et 2 carrés de côté 3.
    Au total, on peut dessiner 20 carrés. Nous dirons que c'est un rectangle-20.
    Quelle est l'aire du rectangle-6400 dont la forme est la plus proche d'un carré ?
    N.B. Les dimensions sont entières tant pour le rectangle que pour les carrés.
Durée environ : 5.7168
"""

from modules.timer import mesure_temps

# Idée :
# On cherche l'ensemble des dimensions (longueur, largeur) qui donne 6400 carrées
# ensuite on trouve la dimension la dimension la plus proche d'un carré en cherchant celle qui a la plus petite différence
# puis on retourne l'aire formé par longueur * largeur

def nombre_carre(L, l):
    """Calcul le nombre de carré à partir de la longueur et de la largeur"""
    m = min(L, l)
    M = max(L, l)
    return m * (m + 1) * (3 * M - m + 1) // 6

def rectangles(nbc):
    """Détermine et retourne l'ensemble de tuples (longueur, largeur) possible"""
    dimensions = set()
    for longueur in range(1, nbc + 1):
        for largeur in range(1, longueur + 1):
            if nombre_carre(longueur, largeur) ==  nbc:
                dimensions.add((longueur, largeur))
                break
    return dimensions

def min_difference(dimensions):
    """Retourne le tuple (longeur, largeur) à la plus faible diff dans l'ensemble"""
    return min(dimensions, key=lambda d: d[0] - d[1])

@mesure_temps
def aire_rectangle(nbc):
    """Retourne l'aire d'un carré (L*l) en connaissant le nombre de carré du rectangle"""
    longeur, largeur = min_difference(rectangles(nbc))
    return longeur * largeur

if __name__ == "__main__":
    print(aire_rectangle(6400))

