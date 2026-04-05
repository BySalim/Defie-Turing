# -*- coding: utf-8 -*-
"""
Auteur : @bysalim
Création : 2026-04-03
Python : 3.14.3
Encodage : UTF-8

Problème 7 :
    En énumérant les six premiers nombres premiers : 2, 3, 5, 7, 11 et 13, on voit que le 6ème nombre premier est 13.
    Quel est le 23456ème nombre premier ?
Version : V1.1
Durée environ : 0.5655 s
"""

from modules.timer import mesure_temps
from modules.utils import est_premier

# Idée :
# On instaure une boucle while qui incrémente un compteur 
# ce compteur est le nombre de nombre premier trouvé
# on commence du début (1) on vérifit chaque nombre en comptant les nombres premiers 
# au 23456ème on retourne le nombre

@mesure_temps
def ieme_nombre_premier(i):
    """Trouve le ième nombre premier"""
    cpt = 0
    n = 0
    while cpt != i:
        n += 1
        if est_premier(n):
            cpt += 1
    return n

if __name__ == "__main__":
    print(ieme_nombre_premier(23456))