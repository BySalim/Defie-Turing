# -*- coding: utf-8 -*-
"""
Auteur : @bysalim
Création : 2026-04-04
Python : 3.14.3
Encodage : UTF-8

Problème 9 :
    Le triplet d'entiers naturels non nuls (a,b,c) est pythagoricien si a^2 + b^2 = c^2.
    Par exemple, (3,4,5) est un triplet pythagoricien.
    Parmi les triplets pythagoriciens (a,b,c) tels que a + b + c = 3600, donner le produit a x b x c le plus grand.
Version : V1.1
Durée environ : 1.1618 s
"""

from modules.timer import mesure_temps

# Idée :
# On a, b et c >= 1
# Avec la formule a + b + c = 3600 on peut en déduire que
# a in [1, 3600 - min(b) - min(c)] == a in [1, 3600 - 2]
# On connait maintenant les valeurs possible de a
# b in [1, 3600 - a - min(c)] == b in [1, 3600 - a - 1]
# On connait maintenant les valeurs possible de b en fonction de a
# D'après la formule a^2 + b^2 = c^2  ==>  c = sqrt(a^2 + b^2)
# On connait maintenant les valeurs possible de c en fonction de a et b
# Il suffit de vérifier que la somme satisfait le résultat a + b + c = 3600
# Si c'est le cas a, b et c sont les valeurs que l'on recherche
# On calcul leur produit et à l'aide d'une variable on stocke la plus grande trouvé

@mesure_temps
def produit_plus_grand_triplets_pythagoriciens(resultat_somme):
    """Retourne le produit le plus grand du triplets pythagoriciens dont la somme égale à [resultat_somme]"""
    
    produit_plus_grand = 0 # Initialisation 
    
    for a in range(1, resultat_somme - 2): # Parcours des valeurs possibles de a
        for b in range(1, resultat_somme - a - 1): # Parcours des valeurs possibles de b
            c = (a**2 + b**2)**0.5 # Calcul c en fonction de a et b
            if (a + b + c) == resultat_somme: # Vérifie si les 3 vérifie la règle
                # Ce qui veut dire que c est un entier mais présenter en réel (ex: 5.0)
                # Alors on le convertie en entier pour avoir un produit entier
                produit = a * b * int(c) # Calcul le produit
                if produit_plus_grand < produit: # Pour stocke le produit le plus grand
                    produit_plus_grand = produit
                break
    return produit_plus_grand

if __name__ == "__main__":
    print(produit_plus_grand_triplets_pythagoriciens(3600))