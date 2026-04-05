"""Ensemble des fonctions utilitaires utilisable dans n'importe quel problem"""

def puissance(n, p):
    """Calcul et retourne n^p"""
    return n ** p

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
    return len(str(nombre))

def produit(iterable):
    """Retourne le produit des éléments d'une liste/tuple/dict/set... en utilisant le cacul basique"""
    p = 1
    for e in iterable:
        p *= e
    return p