"""
Problème : 
    n! signifie n x (n-1) x ... x 3 x 2 x 1
    Par exemple, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800.
    La somme des chiffres du nombre 10! vaut 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
    Trouver la somme des chiffres du nombre 2013!
Durée environ : 0.0354
"""

from modules.timer import mesure_temps
from modules.utils import somme_chiffres, factorielle

# Idée :
# On calculerait le factorielle
# puis on calculerait la somme des chiffres

@mesure_temps
def somme_chiffres_facto(n):
    return somme_chiffres(factorielle(n))

if __name__ == "__main__":
    print(somme_chiffres_facto(2013))