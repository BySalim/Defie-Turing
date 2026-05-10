# -*- coding: utf-8 -*-
"""
Auteur : @bysalim
Création : 2026-04-11
Python : 3.14.3
Encodage : UTF-8

Problème 196 :
    On considère tous les nombres de cinq chiffres que l'on peut composer 
    en utilisant une fois et une seule tous les chiffres impairs : 13579, 13597, 13759, ..., 97531.
    Quelle est la somme de tous ces nombres ?
Version : V2.1
Durée environ : 0.0001240 s
"""

from modules.timer import mesure_temps
from modules.utils import compose_chiffres
from itertools import permutations

# Idée :
# On initialise la liste des chiffres impaires [1, 3, 5, 7, 9]
# On cherche toutes les combinaisons à 5 chiffres possibles et on fait la somme
# C'est une permutation de 5 éléments

@mesure_temps
def solution():
    """"""
    L = [1, 3, 5, 7, 9]
    return sum(compose_chiffres(perm) for perm in permutations(L))
        

if __name__ == "__main__":
    print(solution())
