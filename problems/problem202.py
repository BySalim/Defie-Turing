# -*- coding: utf-8 -*-
"""
Auteur : @bysalim
Création : 2026-05-10
Python : 3.14.3
Encodage : UTF-8

Problème 202 :
    On écrit sur la première ligne d'un tableau de 28 lignes et 37 colonnes 
    les nombres 1, 2, ..., 37. Puis, sur la seconde ligne, 38, ..., 74 et ainsi de suite (de gauche à droite).
    On écrit aussi sur la première colonne les nombres 1, 2, ..., 28. Puis, sur la seconde, 29, ..., 56 et ainsi de suite (de haut en bas).
    Dans certaines cases, les deux nombres seront identiques. Nous les appellerons jumeaux.

    Que vaut la somme des nombres jumeaux ? Chaque nombre jumeau n'est compté qu'une fois.
    
Version : V1.1
Durée environ : 0.0000784 s
"""

from modules.timer import mesure_temps

# Idée :
# Prenons deux matrices formée de lignes et de colonne (28 x 37) nommé A et B
# On remplis la matrice A par ligne colonne commencant par 1
# Puis on remplis la matrice B par colonne ligne commencant par 1
# Les deux tableaux contiennent les mêmes valeurs mais organisées différemment
# Pour i et j allant respectivement de 1 à 28 et de 1 à 37
# A(i,j) = 37 x (i-1) + j et B(i,j) = 28 x (j-1) + i
# La liste des jumeaux sera pour tout i et j, A(i,j) = B(i,j)


@mesure_temps
def solution():
    """"""
    s = 0
    for i in range(1, 29):
        for j in range(1, 38):
            a = 37 * (i-1) + j
            b = 28 * (j-1) + i
            if a == b:
                s += a
    return s
                

if __name__ == "__main__":
    print(solution())
