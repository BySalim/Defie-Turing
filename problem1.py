"""
Problème 1 : Somme de tous les multiples de 5 ou de 7 inférieurs à 2013.
Durée environ : 0.000011 s
"""

from modules.timer import mesure_temps

# Idée : A l'aide de la somme des termes de la suite arithmétique formé par les multiples.

def sum_multiples(n, limit):
    """Calcul la somme des multiples de n inférieur à limit"""
    # Suite arithmétique de premier terme 'n' exemple 5
    # De dernier terme n * i_limite où i_limite est le multiplicateur maximal
    # De nombre de terme i_limite
    premier_terme = n
    dernier_terne = n * (limit // n)
    nombre_termes = limit // n
    return nombre_termes * (premier_terme + dernier_terne) // 2

@mesure_temps
def calc_sum_multiples2(n1, n2, limit):
    """Somme des multiples de 'n1' ou de 'n2' inférieur à 'limit'"""
    return sum_multiples(n1, limit) + sum_multiples(n2, limit) - sum_multiples(n1*n2, limit)

if __name__ == "__main__":
    print(calc_sum_multiples2(5, 7, 2013))
