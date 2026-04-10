# -*- coding: utf-8 -*-
"""
Auteur : @bysalim
Création : 2026-04-10
Python : 3.14.3
Encodage : UTF-8

Problème 146 :
    Thomas est représentant. Il désire inviter chaque semaine un de ses 10 clients à tour de rôle au restaurant, mais selon une fréquence qui serait fonction de la sympathie.
    Il crée 10 fiches, inscrit dessus une note de 1 à 10 et les classe dans l'ordre croissant. Il invite toujours le client correspondant à la fiche de devant. Après le dîner, il classe cette fiche derrière un nombre de fiches correspondant à sa note.

    Classement des cinq premières semaines :

    Semaine 1 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    Semaine 2 [2, 1, 3, 4, 5, 6, 7, 8, 9, 10]
    Semaine 3 [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]
    Semaine 4 [3, 1, 2, 4, 5, 6, 7, 8, 9, 10]
    Semaine 5 [1, 2, 4, 3, 5, 6, 7, 8, 9, 10]

    Quelle semaine le client ayant la note 10 sera pour la première fois en 4ème position dans le classement ?
Version : V1.1
Durée environ : ... s
"""

from modules.timer import mesure_temps

# Idée :
# Chaque client est noté par une note d'empathie de 1 à 10 et classé par ordre
# Chaque semaine un client est invité après cette semaine ce client sera invité après x + 1 semaines où x correspond à sa note d'empathie
# Donc il se place x ième position dans la fiche
# Pour trouver à quelle semaine le client ayant la note 10 sera pour la première fois en 4ème position dans le classement
# Il faudrait une boucle tantque dont le nombre de fois correspond au nombre de semaine
# On s'arréter que lorsque le client ayant la note 10 soit à la 4ème position

@mesure_temps
def solution():
    semaine = 1
    fiche = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    while fiche[3] != 10:
        semaine += 1
        client = fiche.pop(0) # recupére le client
        fiche.insert(client, client) # insert le client a sa nouvelle position qui correspond à 
    return semaine
        

if __name__ == "__main__":
    print(solution())
