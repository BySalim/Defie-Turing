"""
Problème : 
    2^15 = 32768 et la somme de ses chiffres vaut 3 + 2 + 7 + 6 + 8 = 26.
    Que vaut la somme des chiffres composant le nombre 2^2222?
Durée environ : 0.0005
"""

from modules.timer import mesure_temps
from modules.utils import somme_chiffres, puissance

# Idée :
# On calculerait le résultat et on additionnerait chaque chiffre

@mesure_temps
def somme_chiffres_puissance(n, p):
    """Calcul la puissance n^p et retourne la somme des chiffres du résultat"""
    return somme_chiffres(puissance(n, p))

if __name__ == "__main__":
    print(somme_chiffres_puissance(2, 2222))