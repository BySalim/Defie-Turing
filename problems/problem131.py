# -*- coding: utf-8 -*-
"""
Auteur : @bysalim
Création : 2026-04-10
Python : 3.14.3
Encodage : UTF-8

Problème 131 :
    On note S(n) = 1 + 2 + 3 + ... + n la somme des n premiers entiers non nuls.
    De plus, on note I(n) la somme des n premiers entiers inversés.
    On obtient alors, par exemple,
    S(14) = 1 + 2 + 3 + 4 + ... + 10 + 11 + 12 + 13 + 14
    et
    I(14) = 1 + 2 + 3 + 4 + ... + 01 + 11 + 21 + 31 + 41.
    On voit facilement que X=10 est la première valeur pour laquelle S(X) > I(X).
    Quelle sera la somme des entiers "X" inférieurs à un million qui possèdent la propriété S(X) > I(X).
Version : V1.1
Durée environ : 1.5701895 s
"""

from modules.timer import mesure_temps
from modules.utils import decompose_chiffres, compose_chiffres

# Idée :
# Parcours des nombres de 1 à 1'000'000
# Pour chaque nombre on calcul S(n) et I(n)
# On vérifit la condition S(n) > I(n)
# Si c'est le cas on l'ajoute à la somme

@mesure_temps
def solution(limit):
    """
        Retourne la somme des nombres vérifiant la propriété :
        Pour tout n < [limit]:
        S(n) = 1 + 2 + ... + n (somme des entiers de 1 à n)
        I(n) = 1 + 2 + ... + n_inverse (somme des entiers inverse de 1 à n)
        tel que S(n) > I(n)
    """
    somme = 0
    Sn = 0
    In = 0
    for n in range(1, limit):
        Sn += n
        In += compose_chiffres(decompose_chiffres(n, ordre_normal=False))
        if Sn > In:
            somme += n
    return somme

if __name__ == "__main__":
    print(solution(1_000_000))
