# -*- coding: utf-8 -*-
"""
Auteur : @bysalim
Création : 2026-04-09
Python : 3.14.3
Encodage : UTF-8

Problème 85 :
    Il y a 32'490 nombres composés de chiffres tous différents entre 1 et 100'000, par exemple 4, 72, 1'468, 53'920, etc.
    Quelle est la somme de ces nombres ?
Version : V1.1
Durée environ : 0.0784810 s
"""

from modules.timer import mesure_temps
from modules.utils import est_distinct

# Idée :
# On parcourt les nombres depuis le premier
# On vérifit que le nombre est composés de chiffres tous différent
# si oui on l'ajoute dans la somme

@mesure_temps
def somme_nombres_chiffres_differents(nb_nombre):
    """Retourne la somme des [nb_nombre] premiers nombres composés de chiffres tous différents"""
    somme = 0 # Somme des nombres trouvés
    cpt = 0 # compteur des nombres trouvés
    nombre = 1 # nombre à vérifier
    while cpt < nb_nombre: # Tant qu'on a pas atteint le nombre de solution souhaité
        if est_distinct(str(nombre)): # Vérifie que tous les chiffres sont différents
            cpt += 1
            somme += nombre
        nombre += 1
    return somme

if __name__ == "__main__":
    print(somme_nombres_chiffres_differents(32_490))
