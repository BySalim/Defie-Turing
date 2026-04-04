"""
Problème : 
    La somme des nombres premiers entre 1 et 10 vaut 2 + 3 + 5 + 7 = 17.
    Trouver la somme des nombres premiers compris entre 1 et 10'000'000.
Durée environ : 0.4138
"""

from modules.timer import mesure_temps

# Idée :
# En utilisant le Crible d'Ératosthène voir https://fr.wikipedia.org/wiki/Crible_d%27%C3%89ratosth%C3%A8ne

@mesure_temps
def sommes_nombres_premiers(debut, fin):
    """Calcul la somme des nombres premiers se trouvant entre [debut] et [fin] via le Crible d'Ératosthène"""
    # On initialise une liste de byte (faible coût) on considérant que tous les nombres sont premiers
    liste_est_premier = bytearray([True]) * (fin + 1) # l'indice sera le nombre et la valeur sera le booléen
    # 0 et 1 sont exclut
    liste_est_premier[0] = False
    liste_est_premier[1] = False
    
    # On parcours les nombres qui reste c'est à dire les nombres de 2 à sqrt(fin)
    # Si n > sqrt(fin), alors n*n > fin, donc tous ses multiples dépassent fin et sont hors de la liste
    for n in range(2, int(fin**0.5) + 1):
        if liste_est_premier[n]:
            # Si n est premier alors tous ses multiples ne sont pas premiers
            # [n*n::n] est la liste des multiples de n
            nb_multiples = len(liste_est_premier[n*n::n])
            # On modifie les valeurs de ces multiples à False
            liste_est_premier[n*n::n] = bytearray(nb_multiples) # bytearray donne un tableau de 0 (False) au nombre de multiple
          
    # Retourne la somme des   
    return sum(i for i, premier in enumerate(liste_est_premier) if premier and i >= debut)

if __name__ == "__main__":
    print(sommes_nombres_premiers(1, 10_000_000))