# -*- coding: utf-8 -*-
"""
Auteur : @bysalim
Création : 2026-04-04
Python : 3.14.3
Encodage : UTF-8

Problème 11 :
    On appellera "miroir d'un nombre n" le nombre n écrit de droite à gauche. Par exemple, miroir(7423) = 3247.
    Quel est le plus grand nombre inférieur à 10 millions ayant la propriété : miroir(n) = 4 x n ?
Version : V1.3
Durée environ : 2.5051 s
"""

from modules.timer import mesure_temps

# Idée :
# On parcours de 10 millions en décrémentant et on vérifie que la propriété est respecté

def miroir(nombre):
    """Retourne le miroir d'un nombre"""
    return int(str(nombre)[::-1])

@mesure_temps
def plus_grand_nombre(limite):
    """Retourne le plus grand nombre inférieur à [limite] respectant la propriété miroir(n) = 4 x n"""
    for n in range(limite, 0, -1):
        if n * 4 == miroir(n):
            return n

if __name__ == "__main__":
    print(plus_grand_nombre(10_000_000))