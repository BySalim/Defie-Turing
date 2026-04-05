# -*- coding: utf-8 -*-
"""
Auteur : @bysalim
Création : 2026-04-05
Python : 3.14.3
Encodage : UTF-8

Problème 70 :
    Prenons le nombre 102564.
    En faisant passer le dernier chiffre complètement à gauche, on obtient un multiple (différent du nombre de départ).
    En effet, 4 x 102564 = 410256.
    Additionner tous les nombres de 6 chiffres ayant cette propriété.
Version : V1.1
Durée environ : ... s
"""

from modules.timer import mesure_temps

# Idée :
# On parcourt les nombres à 6 chiffres (entre [100_000, 1_000_000[) => [10^(6-1), 10^6 [
# pour chaque nombre on vérifit la propriété si elle est valide on l'ajoute à la somme

@mesure_temps
def somme_curieux_parasite(nb_chiff):
    """
        Retourne la sommme des nombres curieux des nombres à [nb_chiff] chiffres respectant la propriété:
        Un nombre est dit parasite (ou déplaçable par la droite) s'il existe un multiplicateur 
        tel que, lorsqu'on déplace son dernier chiffre à la première position (à gauche), 
        le nouveau nombre obtenu est exactement égal à fois le nombre initial.
    """
    somme = 0
    debut = 10**(nb_chiff - 1)
    fin = debut * 10
    for n in range(debut, fin):
        dernier_chiffre = n % 10
        parasite = dernier_chiffre * 10**(nb_chiff - 1) + n // 10
        if parasite % n == 0 and parasite != n: # si parasite est un multiple de n et n'est n lui même
            print(parasite, n)
            somme += n
    return somme
    

if __name__ == "__main__":
    print(somme_curieux_parasite(6))
