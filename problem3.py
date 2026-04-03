"""
Problème : Quel est le plus grand facteur premier du nombre 20130101 ?
Durée environ : 0.070401 s
"""

import math
from modules.timer import mesure_temps

# Idée : 
# A l'aide d'une boucle de 2 à 'limit div 2' on vérifie 
# que le nombre est premier puis on vérifie autant de fois qu'il peut diviser 'limit' 
# en répétant avec le quotient jusqu'a obtenir 1.

def est_premier(n):
    """Vérifie si un nombre est premier ou pas"""
    if n == 0:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

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

