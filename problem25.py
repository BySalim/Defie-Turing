"""
Problème : 
    La suite de Fibonacci est définie par la relation de récurrence :
    F(n) = F(n-1) + F(n-2) , avec F(1)=1 et F(2)=1.
    Ainsi, les 12 premiers termes sont les suivants : 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
    Le terme de rang 12, F(12), est le premier terme qui comprend 3 chiffres.
    Quel est le rang du premier terme de la suite de Fibonacci qui comprend 2013 chiffres ?
Durée environ : 0.2207885
"""

from modules.timer import mesure_temps
from modules.utils import nb_chiffres

# Idée : 
# on cherche chaque terme de la suite en partant du début on s'arrête lorsque la nombre de chiffre du terme égale à 2013

@mesure_temps
def rang_premier_terme_fib(nb_chiff):
    """Renvoie le rang du premier terme de la suite de fibonnaci ayant [nb_chiff] chiffres"""
    
    terme_actuel  = 0
    terme_suivant = 1
    rang = 0
    
    while nb_chiffres(terme_actuel) != nb_chiff: # ex: on s'arrête que si le nombre de chiffre du terme actuel = 2013
        rang+=1
        terme_actuel, terme_suivant = terme_suivant, terme_actuel + terme_suivant

    return rang

if __name__ == "__main__":
    print(rang_premier_terme_fib(2013))
    