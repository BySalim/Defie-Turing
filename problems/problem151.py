# -*- coding: utf-8 -*-
"""
Auteur : @bysalim
Création : 2026-04-11
Python : 3.14.3
Encodage : UTF-8

Problème 151 :
    2016 est l'aire d'un triangle rectangle, dont les trois côtés forment un triplet pythagoricien.
    Quelles sont les longueurs des côtés a, b et c ? Donner comme réponse le nombre obtenu en juxtaposant a, b et c, avec a < b < c.
Version : V1.1
Durée environ : 0.0018623 s
"""

from modules.timer import mesure_temps

# Idée :
# Un triplet pythagoricien est un triplet d'enter a, b et c non nul vérifiant: a^2 + b^2 = c^2 avec a < b < c
# Surface d'un triangle rectangle = (a × b)/2
# ab = S * 2
# ici S est 2016
# ab = 4032  ==> a vaut au maximum 4032 avec b = 1 et b vaut au minimum a et au maximum b
# Avec deux boucles imbriquées a et b. 
# Le premier allant de 1 à 4032 et le second de 1 à b
# on peut calculer les combinaisons qui ab qui donnent 4032
# et pour chaque ab = 4032 on calcul c = sqrt(a^2 + b^2)
# On suppose que a, b et c sont des entiers

@mesure_temps
def triplet_pythagoricien(aire):
    """Retourne le premier triplet pythagoricien (a, b, c) trouvé en connaisant l'aire"""
    for a in range(1, aire):
        for b in range(a + 1, aire):
            S = (a * b)/2
            if S == aire:
                c = (a**2 + b**2)**0.5
                if c % 1 == 0 :
                    return a, b, int(c)
            elif S > aire:
                break
    
if __name__ == "__main__":
    print(triplet_pythagoricien(2016))
