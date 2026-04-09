# -*- coding: utf-8 -*-
"""
Auteur : @bysalim
Création : 2026-04-09
Python : 3.14.3
Encodage : UTF-8

Problème 77 :
    Deux nombres de 4 chiffres ont la propriété suivante : abcd = ab^2 + cd^2.
    1233 = 12^2 + 33^2
    8833 = 88^2 + 33^2
    Quel est le plus grand nombre de 8 chiffres de ce type : abcdefgh = abcd^2 + efgh^2 ?
Version : V1.1
Durée environ : 1.8951192 s
"""

from modules.timer import mesure_temps
from modules.utils import mini_maxi_par_chiffre
# Idée :
# On parcourt tous les nombres de à 8 chiffres
# On sépare les 4 premiers chiffres et les 4 derniers dans 2 variables différentes
# On vérifie si la somme de leur carré est supérieur égale au nombre
# On commence par le plus grand nombre à 8 chiffres en décrémentant jusqu'au plus petit nombre à 8 chiffres
# Le premier nombre trouver sera le plus grand

@mesure_temps
def nombre_somme_carre(n_chiff):
    """
        Retourne le plus grand nombre à [n_chiff] chiffres qui vérifit la propriété suivante :
        La somme des carrées des deux nombres dont l'un est composé de la moitié supérieur du nombre
        et l'autre la moitié inférieur est égale au nombre lui même. Avec n_chiff un nombre pair.
        Ex (nombre 2 chiffres): 1233 = 12^2 + 33^2
    """
    
    if n_chiff % 2 != 0: # Si le nombre de chiffre n'est pas paire alors il n'y a pas de solution
        print("Aucune solution possible pour un nombre de chiffre impaire")
        return
    
    mini, maxi = mini_maxi_par_chiffre(n_chiff)
    for nombre in range(maxi, mini - 1, -1):
        debut = nombre // 10**(n_chiff // 2) # La moitié supérieur du nombre
        fin = nombre % 10**(n_chiff // 2) # La moitié inférieur du nombre
        if nombre == (debut**2 + fin**2):
            return nombre
    

if __name__ == "__main__":
    print(nombre_somme_carre(8))
