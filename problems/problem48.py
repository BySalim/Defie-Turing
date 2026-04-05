# -*- coding: utf-8 -*-
"""
Auteur : @bysalim
Création : 2026-04-05
Python : 3.14.3
Encodage : UTF-8

Problème 48 :
    1^1 + 2^2 + 3^3 + ... + 10^10 = 10 405 071 317
    Donner les 10 premiers chiffres de la série 1^1 + 2^2 + 3^3 + ... + 2013^2013.
Version : V1.1
Durée environ : 0.0419149 s
"""

from modules.timer import mesure_temps
from modules.utils import nb_chiffres

# Idée :
# On calcul tout et on prend les 10 premiers chiffres

@mesure_temps
def somme_self_puissance(k_terme, n_premiers_chiffre):
    """Retourne les n premiers chiffres de la somme des puissances d'auto référence de 1 au k-ième terme"""
    somme = 0
    for i in range(1, k_terme + 1):
        somme += i**i
    return somme // (10 ** (nb_chiffres(somme) - n_premiers_chiffre))

if __name__ == "__main__":
    print(somme_self_puissance(2013, 10))
