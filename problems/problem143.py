# -*- coding: utf-8 -*-
"""
Auteur : @bysalim
Création : 2026-04-10
Python : 3.14.3
Encodage : UTF-8

Problème 143 :
    Sur un tableau, on écrit tous les entiers positifs 1, 2, 3, ..., N, où N est un entier positif à 7 chiffres.
    Trouver la plus grande valeur possible de N pour laquelle exactement N/2 nombres du tableau contiennent au moins un chiffre 5.
Version : V1.1
Durée environ : 6.3204687 s
"""

from modules.timer import mesure_temps
from modules.utils import mini_maxi_par_chiffre, chiffre_appartient

# Idée :
# On commence par le plus grand entier à 7 chiffres c'est à dire 9'999'999 en décrémentant
# On compte le nombre d'entier inférieur à 10'000'000 contenant le chiffre 5 
# Ce nombre va nous permettre de connaitre toujours le compte sans savoir à tout recalculé
# Pour cela on prend N qui va de 9'999'999 à 999'999 en décrémentant
# On connait le plus grand compte possible qu'on a calculé bien avant
# On vérifit que le compte vaut N//2 si c'est le cas on a notre nombre
# Dans le cas contraire on vérifit que le nombre actuel contient au moins le chiffre 5
# Si c'est le cas on décrémente le compteur (Pourquoi?)
# C'est normale par ce que après N on passe à N-1 
# et si par exemple on avait 5 entiers qui contiennes chiffres 5 au terme N et que N contient également le chiffre 5
# si on passe à N-1 le compteur cpt(N-1) < cpt(N)

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
    cpt = cpt_contenant_chiffre(maxi + 1, chiffre) # On calcul le plus grand compte qu'on peut obtenir
    for N in range(maxi, mini - 1, - 1):
        if cpt == N//2:
            return N
        if chiffre_appartient(chiffre, N):
            cpt -= 1 # On décrémente le nombre trouvé
    

if __name__ == "__main__":
    print(solution(7, 5))
