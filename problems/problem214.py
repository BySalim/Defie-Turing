# -*- coding: utf-8 -*-
"""
Auteur : @bysalim
Création : 2026-05-10
Python : 3.14.3
Encodage : UTF-8

Problème 214 :
    Un nombre entier 10-pandigital est composé de 10 chiffres tous différents. Par exemple : 1234567890 ou 7605483291.
    Donner la somme des nombres entiers 10-pandigitaux qui sont divisibles par tous les entiers inférieurs à 19.
Version : V1.1
Durée environ : 3.0820773 s
"""

from modules.timer import mesure_temps
from modules.utils import compose_chiffres
from itertools import permutations # Pour les permutations des éléments

# Idée :
# Comme le problème 196 on a ici une permutations de 10 chiffres [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# En prenant seulement en compte les nombres formés de 10 chiffres
# Une fois qu'on a ce nombre on vérifie s'il est divisible par tous les entiers inférieurs à 19

def est_divisible_jusqua(n, d):
    for i in range(2, d):
        if n % i != 0 :
            return False
    return True

@mesure_temps
def somme_pandigital_10(D):
    """Retourne la somme des entiers 10-pandigitaux divisibles par tous les entiers inférieurs à [D]"""
    L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    s = 0
    for perm in permutations(L): # permutations permet de permuter les éléments d'une liste chaque itération donne un tuple
        if perm[0] != 0 :
            n = compose_chiffres(perm)
            if est_divisible_jusqua(n, D):
                s += n
    return s

if __name__ == "__main__":
    print(somme_pandigital_10(19))
