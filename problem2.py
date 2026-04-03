"""
Problème 2 : En prenant en compte les termes de la suite de Fibonacci dont les valeurs ne dépassent pas 4 millions, trouver la somme des termes impairs.
Durée environ : 0.000007 s
"""

from modules.timer import mesure_temps

# Idée :
# A l'aide d'une boucle while calculer la somme des termes impaires et le terme suivant 
# tantque le terme suivant n'est pas inférieur à 4 millions
    
@mesure_temps
def sum_odd_terms_fibonacci(limit):
    """Calcul la somme des termes impaires des termes de la suite de Fibonacci inférieurs à 'limit'"""
    current_term = 0
    next_term = 1
    sum_odd_terms = 0
    while next_term < limit:
        if next_term % 2 != 0:
            sum_odd_terms += next_term
        current_term, next_term = next_term, current_term + next_term
    return sum_odd_terms

if __name__ == "__main__":
    print(sum_odd_terms_fibonacci(4_000_000))