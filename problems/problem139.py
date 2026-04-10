# -*- coding: utf-8 -*-
"""
Auteur : @bysalim
Création : 2026-04-10
Python : 3.14.3
Encodage : UTF-8

Problème 139 :
    On lance des fléchettes sur une grille de 100 cases sur 100. Chaque case a la même probabilité d'être touchée.
    Combien faut-il lancer de fléchettes pour que la probabilité d'avoir touché plusieurs fois une même case soit supérieure à 1/2 ?
Version : V1.1
Durée environ : 0.0000429 s
"""

from modules.timer import mesure_temps

# Idée :
# Chaque case a la même probalité d'être touché
# On suppose qu'a chaque lancer la flèche attérit au moins sur une des cases
# Le nombre de case disponible est de 100 x 100 = 10'000
# On cherche le nombre de fléchettes qu'il faut pour que la probabilité de touché plusieur fois la même case soit supérieur à 1/2
# Probabilité que la première flèche touche une case est de P = 10'000/10'000 = 1
# La probalité que la deuxième flèche touche une case différente est de 9'999/10'000
# Pour la troisième flèche on a 9'998/10'000
# On obtient la formule P_non_collision = N/N × (N-1)/N × (N-2)/N × ... × (N-k+1)/N
# C'est la probabilité de toucher toujours des cases différentes après chaque tir
# on cherche le plus petit P_collision > 1/2 avec P_collision = 1 - P_non_colilision
# en faisant varier le k (commencant à 1) on pourra obtenir cette valeur

@mesure_temps
def solution(N):
    k = 1
    P_non_collision = 1
    P_collision = 0
    while P_collision < 0.5:
        k += 1
        P_non_collision *= (N - k + 1)/N
        P_collision = 1 - P_non_collision
    return k

if __name__ == "__main__":
    print(solution(10_000))
