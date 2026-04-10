# -*- coding: utf-8 -*-
"""
Auteur : @bysalim
Création : 2026-04-10
Python : 3.14.3
Encodage : UTF-8

Problème 149 :
    En divisant 100'000'000 par un nombre entier, il peut arriver que le diviseur,
    le quotient et le reste soient composés des mêmes chiffres.
    Plus précisément, tous les chiffres du diviseur sont présents au moins une fois dans le quotient et dans le reste.
    De plus, aucun autre chiffre n'apparaît.
    Voici une possibilité : 100'000'000 / 91'810 = 1089, reste 18'910. Le 1, le 8, le 9 et le 0 apparaissent dans les trois nombres.
    Quelle est l'autre possibilité ? Donnez comme réponse le diviseur.
Version : V1.1
Durée environ : 0.0986416 s
"""

from modules.timer import mesure_temps
from modules.utils import ensemble_chiffres

# Idée :
# On cherche l'autre diviseur qui respecte cette régle
# On commence avec un diviseur qui vaut 1 puis on incrémente à chaque itération
# On vérifit la propriété en calculant le quotient et le reste


def valide(dividende, diviseur):
    """Vérifit que les chiffres du quotient et du reste sont uniquement formé des chiffres du diviseur"""
    
    chiffres_div = ensemble_chiffres(diviseur) # ensemble des chiffres du diviseur
    
    quotient = dividende // diviseur
    reste = dividende % diviseur
    
    chiffres_quotient = ensemble_chiffres(quotient)
    chiffres_reste = ensemble_chiffres(reste)
    return chiffres_quotient == chiffres_div == chiffres_reste
            

@mesure_temps
def solution():
    DIVIDENDE = 100_000_000
    diviseur = 1
    
    while not(valide(DIVIDENDE, diviseur)):
        diviseur += 1
    return diviseur
    

if __name__ == "__main__":
    print(solution())
