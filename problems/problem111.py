# -*- coding: utf-8 -*-
"""
Auteur : @bysalim
Création : 2026-04-10
Python : 3.14.3
Encodage : UTF-8

Problème 111 :
    Quel est le seul nombre n > 1 tel que
    n = d_{k}^{d_{k}} + d_{k-1}^{d_{k-1}} + ... + d_{2}^{d_{2}} + d_{1}^{d_{1}}
    Les di sont les chiffres composant le nombre n.
    Par convention, 0^0 = 1.
Version : V1.1
Durée environ : 0.0016572 s
"""

from modules.timer import mesure_temps
from modules.utils import decompose_chiffres

# Idée :
# On part de 1 en incrémentant chaque fois
# On vérifie chaque nombre en parcourant ses chiffres de la droite à la gauche
# On fait l'équation d_{k}^{d_{k}} + d_{k-1}^{d_{k-1}} + ... + d_{2}^{d_{2}} + d_{1}^{d_{1}}
# Et on vérifie que le résultat est égale à n

@mesure_temps
def solution():
    """
        Retourne le seul nombre respectant la propriété :
        n = d_{k}^{d_{k}} + d_{k-1}^{d_{k-1}} + ... + d_{2}^{d_{2}} + d_{1}^{d_{1}}
        Avec n > 1
    """
    n = 2
    while True:
        resultat = 0 # Stocke le résultat de l'opération
        for c in decompose_chiffres(n):
            resultat += c**c # Ajoute chaque di
        if n == resultat:
            return n
        n += 1

if __name__ == "__main__":
    print(solution())
