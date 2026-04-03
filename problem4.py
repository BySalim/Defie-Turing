"""
Problème : 
    Quel est le plus grand palindrome que l'on peut obtenir 
    en multipliant un nombre de 4 chiffres avec un nombre de 3 chiffres ?
Durée environ : 0.0514
"""

from modules.timer import mesure_temps

# Idée :
# On commencerait par trouver le plus petit et le plus grand nombre de 3 chiffres ainsi que de 4 chiffres.
# Pour trouver le plus grand palindrome il ne suffit pas d'installer deux boucles imbriqués dont l'un commence
# par les plus grandes valeurs et l'autre par les plus petites valeurs ou vice verca 
# Non c'est une erreur car cette façon de faire m'a fait passer à coté du résultat
# En effet pour avoir la plus grande valeur il faut avant tout délimiter les résultats possibles
# en prenant la multiplication des deux petites valeurs comme minimum
# et la multplication des deux plus grandes valeurs comme maximum
# En parcourant cette boucle par le plus grand résultat possible 
# on peut vérifier si ce résultat est divisible par les nombres de 3 chiffres en commencant par le plus grand nombre
# si c'est le cas on vérit que le quotient appartient aux nombres de 4 chiffres.
# Cette facon de faire nous garantit qu'on aurra le plus grand produit.

def est_palindrome(n):
    """Vérifie qu'un nombre est un palindrome"""
    s = str(n)
    return s == s[::-1]

def nombres_limite(t):
    """
    Trouve le plus petit nombre et le plus grand nombre de taille taille t.
    0 exclut.
    Exemple: (1, 9); (10, 99); (100, 999); (1000, 9999); ...
    """
    t = 1 if t < 1 else t
    maxi = (10 ** t) - 1
    mini = (maxi + 1) // 10
    return mini, maxi

def min_max(a, b):
    """Trouve le min et le max entre deux nombres"""
    return (a, b) if a < b else (b, a)

@mesure_temps
def pgp(t1, t2):
    """
    Trouve le plus grand palindromme obtenue en multipliant
    un nombre de [t1] chiffres à un nombre de [t2] chiffres
    """
    # t1 doit être < à t2
    t1, t2 = min_max(t1, t2) # Réordonne pour envisager le cas où c'est désordonné
    
    ppn1, pgn1 = nombres_limite(t1) # le plus petit nombre et le plus grand nombre de la plus petite taille
    ppn2, pgn2 = nombres_limite(t2) # le plus petit nombre et le plus grand nombre de la plus gande taille

    min_res = ppn1 * ppn2 # Plus petit résultat possible
    max_res = pgn1 * pgn2 # Plus grand résultat possible
    
    # Parcours des résultats probables des produits
    for res in range(max_res, min_res+1, -1):
        
        # On vérifie que le résultat est un palindrome sans cela inutile de vérifier les facteurs
        if not est_palindrome(res):
            continue

        # Parcours du prenmier facteur (les nombres t1)
        for a in range(pgn1, ppn1+1, -1):
            # Vérifie si le résultat est divisible par le premier facteur
            if res % a == 0:
                # Si c'est le cas on récupère le multiplicateur
                b = res // a
                # On vérifit que b est fait partie des facteurs seconds
                if ppn2 <= b <= pgn2:
                    # On a alors un produit formé par `a * b = res`
                    # Dont a in [ppn1, pgn1] et b in [ppn2, pgn2]
                    # Et res est un palindrome
                    return res
                
    return -1

print(pgp(4, 3))