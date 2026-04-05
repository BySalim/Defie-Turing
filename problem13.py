# -*- coding: utf-8 -*-
"""
Auteur : @bysalim
Création : 2026-04-04
Python : 3.14.3
Encodage : UTF-8

Problème 13 :
    Le plus petit carré palindrome ayant un nombre pair de chiffres est 698896 = 836^2.
    Quel est le carré palindrome suivant ?
Version : V1.2
Durée environ : 0.2929 s
"""

from modules.timer import mesure_temps
from modules.utils import est_palindrome, nb_chiffres

# Idée :
# On prend comme départ la racine carré du carre palindrome c'est dire 836
# Tant qu'on a pas trouvé on augmente cette valeur de 1
# On vérifie que son carré est un palindrome et que son nombre de chiffre est paire

@mesure_temps
def carre_palindrome_suivant(carre_palin_actuel):
    """Retourne le carre palindrome qui vient après [carre_palin_actuel]"""
    racine_carre = int(carre_palin_actuel**0.5)
    while True:
        racine_carre += 1
        carre = racine_carre**2
        if est_palindrome(carre) and nb_chiffres(carre) % 2 == 0:
            return carre
        
if __name__ == "__main__":
    print(carre_palindrome_suivant(698896))