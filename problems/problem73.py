# -*- coding: utf-8 -*-
"""
Auteur : @bysalim
Création : 2026-04-09
Python : 3.14.3
Encodage : UTF-8

Problème 73 :
    Un nombre entier est un palindrome lorsqu'il peut se lire de droite à gauche comme de gauche à droite. Par exemple, 235532 et 636 sont des palindromes.
    Quel est le plus grand palindrome de 7 chiffres dont le carré est aussi un palindrome ?
Version : V1.1
Durée environ : 2.3880212 s
"""

from modules.timer import mesure_temps
from modules.utils import est_palindrome

# Idée :
# On prcourts les nombres à cette 7 chiffres 
# c'est à dire les nombres se situant entre [10^(7) - 1 ; 10^(7-1)]
# on vérifit que cet nombre est un palindrome si oui on vérifit son carré est également un palindrome
# si tous ces conditions sont respecter on a notre plus grand nombre à 7 chiffre vérifiant les conditions

@mesure_temps
def plus_grand_nombre_palcarre(n_chiff):
    """Retourne le plus grand nombre à [n_chiff] chiffres dont son carré et lui même sont des palindromes"""
    maxi = 10**n_chiff - 1 # Le nombre maximal à [n_chiff] chiffres
    mini = 10**(n_chiff - 1) # Le nombre maximal à [n_chiff] chiffres
    for nombre in range(maxi, mini - 1, - 1): # Parcours des nombres à n_chiff en partant du plus grand
        if est_palindrome(nombre) and est_palindrome(nombre**2):
            return nombre
            

if __name__ == "__main__":
    print(plus_grand_nombre_palcarre(7))
