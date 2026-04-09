# -*- coding: utf-8 -*-
"""
Auteur : @bysalim
Création : 2026-04-09
Python : 3.14.3
Encodage : UTF-8

Problème 107 :
    Nous dirons qu'un entier est pandigital s'il est composé de tous les chiffres de 0 à 9. Par exemple, 1023456789 est le plus petit entier pandigital.
    Quel est le plus petit carré pandigital ?
Version : V1.1
Durée environ : ... s
"""

from modules.timer import mesure_temps
from modules.utils import decompose_chiffres

# Idée :
# Déjà il faut que le nombre est au minimun 10 chiffres
# Donc il faut commencé par la racine de ce nombre
# Incrémenter et vérifie si ce nombre est pandigital

def est_pandigital(nombre):
    """Vérifie qu'un nombre est pandigital c'est à dire qu'il est composé de tous les chiffres de 0 à 9 au moins une fois"""
    chiffres = set() # Ensemble pour stoker les chiffres du nombres un seul fois
    for c in decompose_chiffres(nombre): # Parcours des chiffres du nombre
        chiffres.add(c)
    return len(chiffres) == 10 # A la fin le nombre de chiffres stocker doit être de 10 qui correspond aux chiffre de 0 à 9

@mesure_temps
def plus_petit_carre_pandigital():
    """Retourne le plus petit carré pandigital"""
    racine = int((10**(9))**0.5) # Les pandigital commence à partir des nombres de 10 chiffres
    while True: # On sait qu'il en existe au moins 1 c'est purquoi on se permet
        nombre = racine**2 # calcul du carré
        if est_pandigital(nombre):
            return nombre
        racine += 1

if __name__ == "__main__":
    print(plus_petit_carre_pandigital())
