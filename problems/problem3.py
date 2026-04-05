# -*- coding: utf-8 -*-
"""
Auteur : @bysalim
Création : 2025-11-22
Python : 3.14.3
Encodage : UTF-8

Problème 3 : Quel est le plus grand facteur premier du nombre 20130101 ?
Version : V2.4
Durée environ : 0.070401 s
"""

from modules.timer import mesure_temps
from modules.utils import est_premier

# Idée : 
# A l'aide d'une boucle de 2 à 'limit div 2' on vérifie 
# que le nombre est premier puis on vérifie autant de fois qu'il peut diviser 'limit' 
# en répétant avec le quotient jusqu'a obtenir 1.


@mesure_temps
def grand_facteur_premier(limit):
    """Trouve le plus grand facteur premier de la limite"""
    gfp = 1
    i = 2
    while limit != 1:
        if limit % i == 0:
            # Si ce nombre est premier alors il est le nouveau plus grand facteur premier
            if est_premier(i):
                gfp = i
            
            # On réduit au nombre de fois qu'il y a de puissance de i
            while limit % i == 0:
                limit = limit // i
        i += 1

    return gfp

if __name__ == "__main__":
    print(grand_facteur_premier(20130101))

