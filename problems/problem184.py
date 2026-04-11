# -*- coding: utf-8 -*-
"""
Auteur : @bysalim
Création : 2026-04-11
Python : 3.14.3
Encodage : UTF-8

Problème 184 :
    Le fichier dico.txt contient 323'471 mots français non accentués.
    Un hétérogramme est un mot où chaque lettre apparaît au plus une fois. Voici quelques-uns de ces mots :
    a, je, cage, clapoter, hibou, émir, va-nu-pieds (les traits d'union ne sont pas des lettres), ...
    Par contre, ces mots ne satisfont pas la contrainte :
    enragé (les accents ne comptent pas), capable, ...
    Combien de mots du dictionnaire dico.txt sont des hétérogrammes ?
Version : V1.1
Durée environ : 0.1752880 s
"""

from modules.timer import mesure_temps

# Idée :
# Le fichier dico.txt sera dans files/ accessible à partir de la racine du projet
# On va lire ce fichier ligne par ligne (mot par mot)

FILE_PATH = 'files/dico.txt'

def est_heterogramme(mot):
    """Vérifit qu'un mot est hétérogramme"""
    lettres = set()
    for l in mot:
        if l != '-' and l in lettres:
            return False
        lettres.add(l)
    return True

@mesure_temps
def solution():
    """Compte le nombre d'hétérogramme dans le fichier"""
    cpt = 0
    with open(FILE_PATH, "r") as f:
        for ligne in f:
            if est_heterogramme(ligne.rstrip("\n")):
                cpt += 1
    return cpt
            

if __name__ == "__main__":
    print(solution())
