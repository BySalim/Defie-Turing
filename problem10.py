"""
Problème : 
    La somme des nombres premiers entre 1 et 10 vaut 2 + 3 + 5 + 7 = 17.
    Trouver la somme des nombres premiers compris entre 1 et 10'000'000.
Durée environ : 
"""

from modules.timer import mesure_temps
from modules.utils import est_premier

# Idée :
# 

@mesure_temps
def sommes_nombres_premiers(debut, fin):
    """Calcul la somme des nombres premiers se trouvant entre [debut] et [fin]"""
    somme = 0
    for n in range(debut, fin+1):
        if est_premier(n):
            somme += n
    return somme

if __name__ == "__main__":
    print(sommes_nombres_premiers(1, 10_000_000))