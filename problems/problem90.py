# -*- coding: utf-8 -*-
"""
Auteur : @bysalim
Création : 2026-04-09
Python : 3.14.3
Encodage : UTF-8

Problème 90 :
    276 lampes sont numérotées de 1 à 276.
    Pour passer le temps, 25 enfants appuient sur les interrupteurs à tour de rôle.
    Le premier enfant presse chaque interrupteur.
    Le second presse les boutons 2, 4, 6 , etc. (tous les boutons ayant un numéro multiple de 2),
    le troisième appuie sur les boutons 3, 6, 9, etc.
    Le quatrième presse tous les boutons ayant un numéro multiple de 4, et ainsi de suite jusqu'au 25ème enfant.
    Avant le passage du premier enfant, toutes les ampoules sont éteintes.
    Combien d'ampoules seront allumées après le passage des 25 enfants ?
Version : V1.1
Durée environ : 0.0001645 s
"""

from modules.timer import mesure_temps

# Idée :
# Le premier enfant a allumé toutes les lampes
# Le deuxième est venu eteindre les lampes au numéro pair
# Si on continue comme ca on remarque chaque passage d'enfant peut soit allumer soit éteindre des lampes
# L'algorithme le plus simple à envisager serait de créer un tableau à 277 valeurs dont l'indice correspond au numéro de la lampe (en comptant à partir de 0. On enlèvera cette valeur à la fin)
# C'est un tableau à 1 bytes dont la valeur est soit 1 (True) soit 0 (False)
# Chaque valeur correspond à si l'intérupteur de l'ampoule au numéro est eteinte ou allumé
# Au départ on initialise toutes les valeurs à false pour dire que les ampoules sont eteintes
# Ensuite on parcourt les enfants à partir de 1
# Pour tous les multiples du numéro de l'enfant ont mes le contraire des valeurs qui se trouvent en utilisant le slicing

@mesure_temps
def nombre_ampoules(nb_empoules, nb_enfants):
    """
        Retourne le nombre d'empoules qui seront allumés allumé à la fin du passage des [nb_enfants] enfants en commencant par le premier enfant (plus bas indice).
        Sachant que chaque enfant appuie sur tous les interrupteurs dont le numéro est un multiple du numéro de passage de l'enfant.
    """
    ampoules = bytearray([0]) * (nb_empoules + 1) # Tableau booléens dont chaque valeur correspond à si l'empoule i est eteinte ou allumé
    # L'élement à l'indice 0 est mis pour faciliter l'accès et la compréhension mais il sera pas considéré dans le calcul
    for ie in range(1, nb_enfants + 1): # Parcours des indices d'enfant commencant partir de 1
        ampoules[ie::ie] = bytearray([1 - bool_actuel for bool_actuel in ampoules[ie::ie]]) # On mets l'opposé de chaque valeur dont l'indice est un multiple de l'indice de l'enfant
    return len([x for x in ampoules if x ]) # Calcul du nombre d'ampoule allumé

if __name__ == "__main__":
    print(nombre_ampoules(276, 25))
