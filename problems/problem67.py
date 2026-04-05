# -*- coding: utf-8 -*-
"""
Auteur : @bysalim
Création : 2026-04-05
Python : 3.14.3
Encodage : UTF-8

Problème 67 :
    La suite diatomique de Stern est le résultat des petites équations suivantes:
    s0=0
    s1=1
    s(2n) = s(n)
    s(2n+1) = s(n) + s(n+1)
    Que vaut s(10'000'001) ?
Version : V1.1
Durée environ : 0.0000477 s
"""

from modules.timer import mesure_temps

# Idée :
# on calcul les termes de la suite en commencant à 2 jusqu'au termme 10'000'001
# Comment calculer s(k)?
# s(2n) = s(n) => k = 2n => k est paire => s(k) = s(k/2)
# s(2n+1) = s(n) + s(n+1) => k = 2n+1 => k est impaire => s(k) = 1 + s((k-1)/2+1) 


def _stern(k_terme, _cache = {0: 0, 1: 1}):
    """Calcule le k ième terme de la suite diatomique de stern avec la (Récursivité) et la mémorisation dans le cache"""

    # Cas de base: le terme est 0 ou 1 alors on connais sa valeur
    if k_terme in _cache:
        return _cache[k_terme]
    
    # On applique la formule en fonction de la parité de k et on cacul le terme n
    if k_terme % 2 == 0:
        n = k_terme // 2
        _cache[k_terme] = _stern(n)
    else:
        n = (k_terme - 1) // 2
        _cache[k_terme] = _stern(n) + _stern(n + 1)
   
    return _cache[k_terme]


@mesure_temps
def suite_diatomique_stern(k_terme):
    """Point d'entrée: appel la fonction récursive chargé de calculer le k ième terme de la suite"""
    return _stern(k_terme)


if __name__ == "__main__":
    print(suite_diatomique_stern(10_000_001))
