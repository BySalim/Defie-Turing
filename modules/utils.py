"""Ensemble des fonctions utilitaires utilisable dans n'importe quel problem"""

import math

def somme_chiffres(n):
    """Calcul et retourne la somme des chiffres d'un nombre"""
    s = 0
    while n // 10 != 0:
        chiffre = n % 10
        s += chiffre
        n //= 10 
    return s + n

def factorielle(n):
    """Calcul et retourne le factorielle d'un nombre"""
    fact = 1
    for i in range(n, 1, -1):
        fact *= i
    return fact

def facto_cache(nombre, cache):
    """Retourne la factorielle d'un nombre optimiser via le cache et la (Récursivité)"""
    if nombre in cache:
        return cache[nombre]
        
    if nombre == 0 or nombre == 1:
        # Cas de précaution : cas où le cache ne contiendrait pas les factorielles de 0 ou 1
        return 1
    
    if (nombre - 1) in cache: # Si son prédécesseur est dans la mémoire
        cache[nombre] = nombre * cache[nombre - 1]
    else: 
        # Dans le cas contraire on utilise la récursivité pour calculer son prédecesseur
        # De ce fait on pourra enregistrer chaque prédécesseur (seulement ceux qui nous sont utiles) qui ne sont pas dans la mémoire
        cache[nombre] = facto_cache(nombre - 1, cache)
    
    # On retourne au final la factorielle du nombre calculer
    return cache[nombre]
    

def est_premier(n):
    """Vérifie si un nombre est premier ou pas"""
    if n == 0 or n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def est_palindrome(n):
    """Vérifie qu'un nombre est un palindrome"""
    s = str(n)
    return s == s[::-1]

def nb_chiffres(nombre):
    """Retourne le nombre de chiffre d'un nombre"""
    return int(math.log10(nombre)) + 1

def produit(iterable):
    """Retourne le produit des éléments d'une liste/tuple/dict/set... en utilisant le cacul basique"""
    return math.prod(iterable)

def mini_maxi_par_chiffre(nb_chiffres):
    """Retourne le plus petit entier et le plus grand entier qui ont [nb_chiffres] chiffres"""
    return 10**(nb_chiffres - 1), 10**nb_chiffres - 1


def est_identique(iterable):
    """Vérifie si tous les éléments de l'itérables sont les mêmes"""
    for i in range(len(iterable)-1):
        if iterable[i] != iterable[i+1]: # Si l'élément actuel est différent de l'élément suivant
            return False
    # Si tous les éléments sont identiques
    return True

def est_distinct(iterable):
    """Vérifie que tous les éléments d'un iterable sont différents"""
    distinct = set()
    for e in iterable:
        if e in distinct:
            return False
        distinct.add(e)
    return True

def decompose_chiffres(nombre):
    """Transforme un nombre en une liste de ses chiffres"""
    l = []
    while nombre != 0:
        l.append(nombre % 10)
        nombre //= 10
    l.reverse()
    return l

def compose_chiffres(chiffres):
    """Transforme une liste de chiffre en son nombre"""
    nombre = 0
    for c in chiffres:
        nombre = nombre * 10 + int(c)
    return nombre
    
if __name__ == "__main__":
    print(decompose_chiffres(7445882))
    print(compose_chiffres([7, 4, 4, 5, 8, 8, 2]))