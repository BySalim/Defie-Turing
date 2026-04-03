"""
Problème : 
    2^15 = 32768 et la somme de ses chiffres vaut 3 + 2 + 7 + 6 + 8 = 26.
    Que vaut la somme des chiffres composant le nombre 2^2222?
Durée environ : 0.0005
"""

from modules.timer import mesure_temps

# Idée :
# On calculerait le résultat et on aditionnerait chaque chiffre

def addition_chiffres(n):
    """Calcul et retourne la somme des chiffres d'un nombre"""
    s = 0
    while n // 10 != 0:
        chiffre = n % 10
        s += chiffre
        n //= 10 
    return s + n

@mesure_temps
def somme_chiffres_puissance(n, p):
    """Calcul n^p et retourne la somme des chiffres du résultat"""
    res = n ** p
    return addition_chiffres(res)

if __name__ == "__main__":
    print(somme_chiffres_puissance(2, 2222))