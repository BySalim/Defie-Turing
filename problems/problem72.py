# -*- coding: utf-8 -*-
"""
Auteur : @bysalim
Création : 2026-04-09
Python : 3.14.3
Encodage : UTF-8

Problème 72 :
    Parmi tous les entiers inférieurs à 1 milliard, combien sont des carrés se terminant par exactement 3 chiffres identiques ?
    Par exemple, 213444 = 462^2
Version : V1.1
Durée environ : 0.0145254 s
"""

from modules.timer import mesure_temps

# Idée :
# On parcourt les nombres entre 10 et < sqrt(1 millards). Pourquoi 10 car c'est à partir de 10 que le carré d'un nombre donne au minimum 3 chiffres
# Pour chaque nombre on récupère les trois derniers chiffres il suffit d'utiliser la formule suivante
# nombre = nombre % 10 ^ 3
# Pour une solution général on va prendre n pour le nombre de derniers chiffres identique et limite pour le nombre maximal à ne pas atteindre

def elements_identique(iterable):
    """Vérifie si tous les éléments de l'itérables sont les mêmes"""
    for i in range(len(iterable)-1):
        if iterable[i] != iterable[i+1]: # Si l'élément actuel est différent de l'élément suivant
            return False
    # Si tous les éléments sont identiques
    return True
        

@mesure_temps
def count_carre_n_chiffres_identique(n, limit):
    """Compte le nombre d'entier dont les [n] derniers chiffres de leur carré sont identique et que le carré de l'entier soit inférieur à [limit]"""
    
    cpt = 0 # Compteur
    debut = int((10**(n-1))**0.5 + 0.5) # C'est le plus petit nombre dont le carré à au moins n chiffres
    
    for nombre in range(debut, int(limit ** 0.5) + 1): # parcours des nombres 
        carre = nombre ** 2 
        
        n_last_chiffres = str(carre % (10 ** n)) # Les n derniers chiffres de chaque nombre en chaine
        if len(n_last_chiffres) == n : # Si les chiffres valent le nombre requit car il se peut qu'on ait (001) qui a été convertie en 1 les chiffres 0 sont exclues du compte
            if elements_identique(n_last_chiffres): # Si tous les chiffres sont identiques
                cpt += 1
                
    return cpt

if __name__ == "__main__":
    print(count_carre_n_chiffres_identique(3, 1_000_000_000))
