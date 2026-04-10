# -*- coding: utf-8 -*-
"""
Auteur : @bysalim
Création : 2026-04-10
Python : 3.14.3
Encodage : UTF-8

Problème 126 :
    Pierre de Fermat (1601?-1665) désigne par le terme "sous-double" un entier dont la somme de ses diviseurs propres est égale au double de ce nombre.
    Par exemple, la somme des diviseurs propres de 120 est égale à :
    1 + 2 + 3 + 4 + 5 + 6 + 8 + 10 + 12 + 15 + 20 + 24 + 30 + 40 + 60 = 240.
    De même, il désigne par le terme "sous-triple" un entier dont la somme de ses diviseurs propres est égale au triple de ce nombre.
    Donner la somme des sous-triples inférieurs à 100'000.
Version : V1.1
Durée environ : 0.8962693 s
"""

from modules.timer import mesure_temps
from modules.utils import somme_diviseurs_propres

# Idée :
# On parcout les nombres inférieurs à 100'000 en commencant par 1
# On vérifit que chaque nombre est un sous-triple (comment?)
# Pour le savoir on fait la somme de ses diviseurs et on vérifit que le résultat est égale au triple du nombre lui même


def est_sous_triple(nombre):
    """Vérifit qu'un nombre est un sous triple"""
    return somme_diviseurs_propres(nombre) == (3 * nombre)

@mesure_temps
def somme_sous_triples(limit):
    """Retourne la somme des sous-triples inférieur à [limit]"""
    somme = 0
    for n in range(1, limit):
        if est_sous_triple(n):
            print(n)
            somme += n
    return somme

if __name__ == "__main__":
    print(somme_sous_triples(100_000))
