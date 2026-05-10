# -*- coding: utf-8 -*-
"""
Auteur : @bysalim
Création : 2026-05-10
Python : 3.14.3
Encodage : UTF-8

Problème 222 :
    Soit une rangée de 8000 lampes. Initialement, seule celle située tout à gauche est allumée.
    Ensuite, toutes les secondes, l'opération suivante est réalisée: chaque lampe change d'état (allumée ou éteinte) si celle située à sa gauche était allumée une seconde avant. La lampe la plus à gauche reste allumée tout le temps. Cette opération est instantanée.
    Le processus s'arrête lorsque la lampe située à l'extrémité droite s'allume pour la première fois.
    Combien de lampes sont alors allumées?
Version : V1.1
Durée environ : 2.8886514 s
"""

from modules.timer import mesure_temps

# Idée :
# On initialise un liste d'ampoules éteintes on allume la première et on s'assure qu'elle reste toujours allumé
# On s'arrétera que lorsque la dernière lammpe (8000ième) qui est la lampe la plus à droite soit allumé
# A chaque tour parcours les lampes en commencant par la dernière et on change l'état de la lampe si la lampe qui vient avant (à gauche) est allumé
# On retourne le nombre de lampe allumé à la fin

@mesure_temps
def solution(nb_lampes):
    lampes = bytearray(nb_lampes) # On initialise toutes les lampes comme éteintes
    lampes[0] = 1 # On allume la première lampe (lampe la plus à gauche)
    while lampes[-1] != 1: # Tantque la dernière lampe n'est pas allumée
        for i in range(nb_lampes-1, 0, -1): # Parcours commencant à l'ampoule la plus à droite
            if lampes[i-1] == 1: # Si la lampe qui vient avant (dans le classement) est allumé
                lampes[i] ^= 1 # XOR on allume la lampe si elle était eteinte et on l'eteint si elle etait allumé
    return sum(lampes)
    

if __name__ == "__main__":
    print(solution(8000))
