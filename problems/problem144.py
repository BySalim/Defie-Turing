# -*- coding: utf-8 -*-
"""
Auteur : @bysalim
Création : 2026-04-10
Python : 3.14.3
Encodage : UTF-8

Problème 144 :
    Combien y a-t-il de nombres de six chiffres où le 7 n'apparaît qu'une fois et où il représente le chiffre le plus élevé ?
    Par exemple : 253753, 111172, 744252, etc.
Version : V1.1
Durée environ : 0.4059937 s
"""

from modules.timer import mesure_temps
from modules.utils import mini_maxi_par_chiffre

# Idée :
# On parcourt les nombres à 6 chiffres
# On vérifit que dans ce nombre il y a un unique 7 et qu'il soit le plus
# On compte le nombre d'entier validé

def present_unique_plus_grand(chiffre, nombre):
    """Vérifie qu'un chiffre est présent une seul fois dans un nombre et qu'il soit le plus grand chiffre"""
    cpt = 0
    while nombre != 0:
        c = nombre % 10
        
        if chiffre < c :
            return False
        elif chiffre == c :
            cpt += 1
            
        nombre //= 10
    return cpt == 1
        

@mesure_temps
def solution(n_chiff, chiffre):
    """Retourne le nombre d'entier à [n_chiff] qui ont un unique chiffre [chiffre] et que ce chiffre soit son plus grand chiffre"""
    cpt = 0
    mini, maxi = mini_maxi_par_chiffre(n_chiff)
    for n in range(mini, maxi + 1):
        if present_unique_plus_grand(chiffre, n):
            cpt += 1
    return cpt


if __name__ == "__main__":
    print(solution(6, 7))
