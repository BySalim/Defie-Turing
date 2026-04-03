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

def est_premier(n):
    """Vérifie si un nombre est premier ou pas"""
    if n == 0 or n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True