# -*- coding: utf-8 -*-
"""
Auteur : @bysalim
Création : 2026-04-10
Python : 3.14.3
Encodage : UTF-8

Problème 132 :
    La moyenne des carrés des nombres entiers de 1 à 5 est égale à (1+4+9+16+25)/5 = 11.
    La moyenne des carrés des nombres entiers de 1 à 77 est égale à 2015.
    Combien de nombres entiers positifs strictement inférieurs à un milliard 
    sont égaux à la moyenne des carrés des nombres entiers consécutifs de 1 jusqu'à un certain nombre ?
    Note : la moyenne d'un seul nombre est égale à ce nombre.
Version : V1.1
Durée environ : 0.0161295 s
"""

from modules.timer import mesure_temps

# Idée :
# On parcourt les nombres à partir de 1
# On calcul et on mets à jour la somme des carrés consécutifs trouvés par exemple S(n) = S(n-1) + n^2 avec S(0) = 0
# On calcule la moyenne : M(n) = S(n) / n
# La première condition est que la valeur M(n) doit être un entier
# Si c'est le cas on compte ce nombre
# On s'arrétra seulement quand M(n) >= 1'000'000'000

@mesure_temps
def nombre_moy_carres_consecutif(limit):
    """Retourne le nombre de moyenne des carrés consécutifs possible avec la moyenne < [limit]"""
    cpt = 0
    Sn = 0
    Mn = 0
    n = 1
    while Mn < limit:
        Sn += n**2
        Mn =  Sn / n
        if Mn.is_integer():
            cpt += 1
        n += 1
    return cpt
        

if __name__ == "__main__":
    print(nombre_moy_carres_consecutif(1_000_000_000))
