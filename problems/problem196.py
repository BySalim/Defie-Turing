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
Version : V1.1
Durée environ : 0.0001287 s
"""

from modules.timer import mesure_temps
from modules.utils import factorielle, compose_chiffres

# Idée :
# On initialise la liste des chiffres impaires [1, 3, 5, 7, 9]
# On cherche toutes les combinaisons à 5 chiffres possibles et on fait la somme
# C'est une permutation de 5 éléments donc le nombre total possible est 5!

@mesure_temps
def solution():
    """"""
    L = [1, 3, 5, 7, 9]
    s = 0
    k = 0 # Indice pour la permutation des chiffres
    N = len(L)
    for _ in range(factorielle(5)):
        # On rassemble les chiffres dans l'ordre pour former le nombre puis on l'ajoute à la somme
        s += compose_chiffres(L)
        # On permute le chiffre actuel et le suivant
        L[k], L[k+1] = L[k+1], L[k]
        # On vérifit si on est arrivé à la fin de la liste
        if k+1 == N-1:
            # Dans ce cas on recommence à zero
            k = 0
        else:
            k+=1
    return s
        

if __name__ == "__main__":
    print(solution())
