# -*- coding: utf-8 -*-
"""
Auteur : @bysalim
Création : 2026-04-09
Python : 3.14.3
Encodage : UTF-8

Problème 109 :
    Un cryptarithme est un casse-tête numérique et logique 
    qui consiste en une équation mathématique où les lettres représentent des chiffres à trouver.
    CHAT + CHAT = MINOU
    Soit x la plus petite valeur possible de MINOU et y la plus grande. Que vaut x + y ?
Version : V1.1
Durée environ : 0.0189910 s
"""

from modules.timer import mesure_temps
from modules.utils import est_distinct

# Idée :
# C H A T et M I N O U sont des chiffres distincts 
# On va chercher à créer le nombre CHAT en utilisant 4 boucles imbirquées pour les 4 chiffres C H A T qui vont de 0 à 9
# On ensemble les chiffres dans chat
# En calcul le nombre MINOU = 2 * CHAT 
# On vérifit que tous les chiffres formée par MINOU et CHAT sont distincts et que MINOU a bien 5 chiffres
# Si toutes ces conditions sont validées ont stocke le nombre MINOU dans une liste
# A la fin le premier élément de la liste correspondra à x et le dernier élément de la liste correspondra à y

@mesure_temps
def cryptarithme():
    """
        Retourne la somme du plus petit MINOU et du plus grand MINOU verifiant la propriété suivante:
        CHAT + CHAT = MINOU
    """
    possibles = []
    for c in range(10):
        for h in range(10):
            for a in range(10):
                for t in range(10):
                    chat = f"{c}{h}{a}{t}"
                    minou = str(2 * int(chat))
                    if est_distinct(chat + minou) and len(minou) == 5:
                        possibles.append(int(minou))
    return possibles[0] + possibles[-1]

if __name__ == "__main__":
    print(cryptarithme())
