"""
Problème : 
    En mathématiques, on appelle "suite de Syracuse" une suite d'entiers naturels définie de la manière suivante :
    On part d'un nombre entier plus grand que zéro ; s’il est pair, on le divise par 2 ; s’il est impair, on le multiplie par 3 et on ajoute 1.
    En répétant l’opération, on obtient une suite d'entiers positifs dont chacun ne dépend que de son prédécesseur.
    Il existe une conjecture qui dit que la suite de Syracuse de n'importe quel entier strictement positif atteint 1.
    Par exemple, à partir de 14, on construit la suite des nombres : 14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1.
    C'est ce qu'on appelle la suite de Syracuse du nombre 14. Elle a ici une longueur de 18.
    Pour quel nombre de départ inférieur à 1'500'000 obtient-on la plus longue suite de Syracuse? Il y a deux solutions, donner la plus petite.
Durée environ : 1.6468
"""

from modules.timer import mesure_temps

# Idée :
# on initialise la taille maximale et le nombre qui contient la plus grande suite
# On cherche toutes les suites de syracuse en partant de 1 et en s'arrétant à 1'500'000
# on calcule la taille de la suite actuel et on vérifie si elle est 'strictement' plus grande que les anciennes
# si oui on stocke son nombre et on met à jour la nouvelle taille maximale
# le choix du parcours (1 à 1'500'000) et la condition de mise à jour du maximum (>)
# nous permet d'avoir à la fin le plus petit nombre qui a la plus grande suite de syracuse

def longueur_syracuse(nombre_depart, cache = {1:1}):
    """Renvoie la taille de la suite (liste) de Syracuse à partir du [nombre_depart] optimiser avec la mémoire (cache)"""
    
    if nombre_depart in cache:
        # Cas de base on retourne la longueur si le nombre de départ est déjà présent dans le cache
        return cache[nombre_depart]
    
    # On caclul le nombre suivant
    suivant = nombre_depart
    if suivant % 2 == 0:
        suivant //= 2
    else:
        suivant = suivant * 3 + 1
    
    # Récurrence: système backtraking qui va calculer la longueur de chaque élément de la suite
    cache[nombre_depart] = 1 + longueur_syracuse(suivant, cache)
    return cache[nombre_depart]

@mesure_temps
def plus_petit_nombre_depart_suite_syracuse_plus_longue(limit):
    """Retourne le plus petit nombre de depart inférieur à limit ayant la plus longue suite de Syracuse optimiser avec la mémoire (cache)"""
    cache = {1: 1}
    min_depart = 1
    max_long = 0

    for nombre in range(1, limit + 1):
        taille_suite = longueur_syracuse(nombre, cache)
        if taille_suite > max_long:
            max_long = taille_suite
            min_depart = nombre
    return min_depart

if __name__ == "__main__":
    print(plus_petit_nombre_depart_suite_syracuse_plus_longue(1_500_000))