# -*- coding: utf-8 -*-
"""
Auteur : @bysalim
Création : 2026-04-05
Python : 3.14.3
Encodage : UTF-8

Problème 34 :
    145 est un nombre curieux. En effet, 1! + 4! + 5! = 1 + 24 + 120 = 145.
    Trouver le produit de tous les nombres qui sont égaux à la somme de la factorielle de leurs chiffres.
    Remarques:
    1! = 1 et 2! = 2 ne sont pas des sommes et ne seront pas incluses dans le produit.
    Rappelons que 0! = 1
Version : V1.1
Durée environ : 17.9669423 s
"""

from modules.timer import mesure_temps
from modules.utils import facto_cache, produit

# Idée :
# Pour chercher les nombres curieux on commencerait à partir de 3 car 1 et 2 sont exlus d'après l'énoncer
# L'énoncer n'a pas donné de borne supérieur au problème mais d'après mes recherches le problème est mathématiquement borné
# Dans un nombre à n chiffres la valeur maximale est 10^n - 1. ex: 3 chiffres -> 999 (plus grand nombre à 3 chiffres)
# Dans un nombre à n chiffres la valeur minimale est 10^(n - 1). ex: 3 chiffres -> 100 (plus petit nombre à 3 chiffres)
# Prenons les nombres à 1 chiffre la plus grande est 9 et la somme maximale de ses factorielles est 9!
# Ensuite les nombres à 2 chiffres la plus grande est 99 et la somme maximale de ses factorielles est 9! + 9! aussi égale à 2 * 9!
# Si l'on continue on remarque que la somme maximale des factorielles d'un nombre à n chiffres est au maximum n * 9! = n * 362 880
# Mais à certain nombre de chiffre le nombre est beaucoup plus grand que la somme ses factorielles
# En effet à partir d'un certains point le nombre croit beaucoup plus vite que la somme maximale possible
# Ex: 
# - 6 chiffres : 6 * 362 880 = 2 177 280 et le plus grand nombre de 6 chiffres est 999 999 et le plus petit vaut 100 000
# - 7 chiffres : 7 * 362 880 = 2 540 160 et le plus grand nombre de 7 chiffres est 9 999 999 et le plus petit vaut 1 000 000
# - 8 chiffres : 8 * 362 880 = 2 903 040 et le plus grand nombre de 8 chiffres est 99 999 999 et le plus petit vaut 10 000 000
# On remarque à partir d'un certain niveau les nombres à 7 chiffres sont plus grand que la somme maximale des factorielles
# La limite visible est donc le nombre maximal à 7 chiffres 9 999 999
# Donc théoriquement on devrait s'arréter à 9 999 999

def somme_factorielle_chiffre(nombre, Factorielles):
    """Retourne la somme des factorielles des chiffres d'un nombre. Optimiser avec la mémoire: Garde les valeurs déjà calculer"""
    return sum(facto_cache(int(d), Factorielles) for d in str(nombre))

def nombres_curieux_facto():
    """
    Retourne les nombres curieux.
    Les nombres curieux sont les nombres dont la somme 
    des factorielles de ses chiffres est égale à lui mème.
    Pour une meilleur optimisation on va stoker les factorielles et leur valeur dans un dictionnaire.
    """
    
    LIMITE = 9_999_999 # Limite appliquer
    # initialiser pour les premières valeurs rapides 0, 1 et 2
    Factorielles = {
        0: 1, 
        1: 1, 
        2: 2
    }
    curieux = []
    nombre = 3 # On commence à 3 car 1 et 2 sont exclus d'après l'énoncé
    
    # Tantque la somme facto des chiffres n'ait pas dépasser le nombre lui même
    while nombre <= LIMITE:
        if somme_factorielle_chiffre(nombre, Factorielles) == nombre:
            # alors c'est un nombre curieux 
            curieux.append(nombre)
        
        nombre += 1
    
    return curieux

@mesure_temps
def produit_nombres_curieux_facto():
    """Retourne le produit des nombres curieux trouvé"""
    return produit(nombres_curieux_facto())

if __name__ == "__main__":
    print(produit_nombres_curieux_facto())
        