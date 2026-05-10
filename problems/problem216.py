# -*- coding: utf-8 -*-
"""
Auteur : @bysalim
Création : 2026-05-10
Python : 3.14.3
Encodage : UTF-8

Problème 216 :
    Un nombre palindrome est un nombre qu'on lit de la même manière de gauche à droite et de droite à gauche, comme par exemple 12321.
    On calcule la somme des carrés des nombres entiers naturels, dans l'ordre : 0^2 + 1^2 + 2^2 + 3^2 + 4^2 + ...
    On arrêtera le calcul dès que, après avoir ajouté le carré d'un nombre palindrome ayant au moins deux chiffres, on obtiendra une somme qui est aussi un nombre palindrome.
    Quelle sera alors cette somme ?
Version : V1.1
Durée environ : 0.0001404 s
"""

from modules.timer import mesure_temps
from modules.utils import nb_chiffres, est_palindrome

# Idée :
# On parcout les nombres commencant par 0 on s'arréte que lorsque le nombre actuel est un palindromme à au moins de chiffre
# et que la somme des carrés jusque là donne un palindrome

@mesure_temps
def solution():
    """"""
    n = 1
    s = 0
    while True:
        s += n*n # Somme des carrées
        if nb_chiffres(n) >= 2 and est_palindrome(n) and est_palindrome(s):
            break
        n += 1
    return s
        

if __name__ == "__main__":
    print(solution())
