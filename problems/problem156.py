# -*- coding: utf-8 -*-
"""
Auteur : @bysalim
Création : 2026-04-11
Python : 3.14.3
Encodage : UTF-8

Problème 156 :
    On dit que 7 est une puissance finale pour 3, car 3^7 = 2187 (le dernier chiffre est 7).
    Quelle est la plus petite puissance finale pour 18 ? Autrement dit,
    quel est le plus petit entier n tel que l'écriture décimale de 18^n se termine par celle de n ?
Version : V1.1
Durée environ : 0.0000520 s
"""

from modules.timer import mesure_temps
from modules.utils import nb_chiffres

# Idée :
# On parcours les puissances à partir de 1
# On vérifit que 18^n se termine n

@mesure_temps
def puissance_finale(nbr):
    """Retourne la plus petite puissance de [nbr] qui se termine par la puissance elle même"""
    n = 1
    while n < 1_000_000: # limite d'itération
        
        if (nbr**n) % 10**nb_chiffres(n) == n:
            return n
        n += 1
    return n
        

if __name__ == "__main__":
    print(puissance_finale(18))
