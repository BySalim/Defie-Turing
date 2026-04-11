# -*- coding: utf-8 -*-
"""
Auteur : @bysalim
Création : 2026-04-11
Python : 3.14.3
Encodage : UTF-8

Problème 162 :
    On multiplie entre eux trois nombres pairs strictement positifs consécutifs. On obtient un nombre palindrome.
    Quel est le plus petit nombre palindrome ainsi obtenu ?
Version : V1.1
Durée environ : ... s
"""

from modules.timer import mesure_temps
from modules.utils import est_palindrome

# Idée :
# On initialise le premier nombre a à 2 (car le plus petit entier pair est 2)
# les deux autres nombres pairs consécutifs seront calculés par (a+2) et (a+4)
# On vérifit que le produit est un palindrome

@mesure_temps
def solution():
    """Retourne le plus petit palindrome dont le produit qui est égale à produit de trois entiers consécutifs"""
    a = 2
    while a < 1_000_000: # Maximum d'itération
        prod = a * (a + 2) * (a + 4)
        if est_palindrome(prod):
            return prod
        a += 2
    

if __name__ == "__main__":
    print(solution())
