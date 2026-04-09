# -*- coding: utf-8 -*-
"""
Auteur : @bysalim
Création : 2026-04-09
Python : 3.14.3
Encodage : UTF-8

Problème 78 :
    Quel est le seul nombre ayant le motif suivant : abcd = a^b x c^d ?
    Précision (1.5.2014) : ce n'est pas un cryptarithme. Deux lettres différentes peuvent désigner le même chiffre.
Version : V1.1
Durée environ : 0.0011661 s
"""

from modules.timer import mesure_temps
from modules.utils import mini_maxi_par_chiffre

# Idée :
# On recherche le seul nombre vérifiant la propriété
# On peut parcourir tout les nombres à 4 chiffres
# On retourne le premier nombre qui respecte la propriété

@mesure_temps
def solution():
    """
        Retourne le premier nombre à 4 vérifiant cette propriété :
        abcd = a^b x c^d
    """
    mini, maxi = mini_maxi_par_chiffre(4) # Obtient les bornes des nombres à 4 chiffres
    for nombre in range(mini, maxi + 1):
        a, b, c, d = [int(chiffre) for chiffre in str(nombre)] # Transforme le nombre en chaine puis partage chaque chiffre entre a, b, c et d
        if nombre == (a**b * c**d):
            return nombre
    return None


if __name__ == "__main__":
    print(solution())
