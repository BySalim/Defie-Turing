# -*- coding: utf-8 -*-
"""
Auteur : @bysalim
Création : 2026-04-10
Python : 3.14.3
Encodage : UTF-8

Problème 143 :
    Sur un tableau, on écrit tous les entiers positifs 1, 2, 3, ..., N, où N est un entier positif à 7 chiffres.
    Trouver la plus grande valeur possible de N pour laquelle exactement N/2 nombres du tableau contiennent au moins un chiffre 5.
Version : V2.1
Durée environ : 4.3345499 s
"""

from modules.timer import mesure_temps
from modules.utils import mini_maxi_par_chiffre, chiffre_appartient

# Idée :
# On commence par le plus grand entier à 7 chiffres c'est à dire 9'999'999 en décrémentant
# On compte le nombre d'entier inférieur à 1'000'000 contenant le chiffre 5 (plus petit compte possible)
# Ce nombre va nous permettre de connaitre toujours le compte sans savoir à tout recalculé
# Pour cela on prend N qui va de 1'000'000 à 10'000'000
# On connait le plus petit compte possible qu'on a calculé bien avant
# On vérifit que le nombre actuel contient au moins le chiffre 5
# Si c'est le cas on incrémente le compteur
# On vérifit que le compte vaut N//2 si c'est le cas on a notre nombre
# AVEC CETTE VERSION ON FAIT MOIN DE CALCUL

def cpt_contenant_chiffre(limit, chiffre):
    """Retourne le nombre d'entier inférieur à [limit] contenant au moins un chiffre [chiffre]"""
    cpt = 0
    for n in range(limit):
        if chiffre_appartient(chiffre, n):
            cpt += 1
    return cpt

@mesure_temps
def solution(n_chiff, chiffre):
    """
        Retourne N le plus grand entier possible à [n_chiff] chiffres
        pour lequel on a exactement les entiers consécutifs inférieurs on a
        N/2 nombres contenant au moins le chiffre [chiffre]
    """
    mini, maxi = mini_maxi_par_chiffre(n_chiff)
    cpt = cpt_contenant_chiffre(mini, chiffre) # On calcul le plus petit compte qu'on peut obtenir en dessous de la valeur minimal
    plus_grand_trouve = mini # Stocke la plus grande valeur trouvé
    for N in range(mini, maxi + 1):
        
        if chiffre_appartient(chiffre, N):
            cpt += 1 # On incrément si le nombre contient le chiffre
            
        if cpt == N//2 : # On vérifit le compte
            plus_grand_trouve = N # Stoke la nouvelle valeur
    return plus_grand_trouve

if __name__ == "__main__":
    print(solution(7, 5))
