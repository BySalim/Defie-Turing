# -*- coding: utf-8 -*-
"""
Auteur : @bysalim
Création : 2026-04-09
Python : 3.14.3
Encodage : UTF-8

Problème 71 :
    567^2 = 321489
    Cette équation utilise tous les chiffres de 1 à 9, une fois chacun (si on excepte le carré).
    Quel est le seul autre nombre qui, élevé au carré, présente la même propriété ?
    
Version : V1.1
Durée environ : 0.0012963 s
"""

from modules.timer import mesure_temps

# Idée :
# On cherche un autre nombre qui respecte cette propriété
# Une boucle tantque nous permettra de vérifier les nombres à partir de 1
# Si le nombre vérifit la propriété et n'est pas égale à 567
# Comment va t'on vérifier la proprité ?
# Il faut avoir dans la concaténation du nombre et de son carré tous les chiffres de 1 à 9 une fois chacun
# Donc on concactene les deux valeurs on vérifie que la taille ne vaut pas 9 chiffres si c'est le cas il respecte déjà pas la propriété
# Dans le cas contraire on parcours chaque chiffre et à l'aide d'un ensemble vide au départ on enregistre chaque chiffre trouvé
# Si un des chiffres est 0 on sort
# Si un des chiffres est présent plus d'une fois on sort également
# Une fois toute ces conditions respecter on aurra notre nombre

@mesure_temps
def currieux_chiffre_1_9():
    """
        Permet de trouver le nombre autre que 567 qui vérifit la propriété:
        nombre^2 = carre_nombre utilise tous les chiffres de 1 à 9, une fois chacun (si on excepte le carré)
    """
    nombre = 1
    while True:
        if nombre != 567 : 
            concatenation = f"{nombre}{nombre ** 2}" # Concaténation du nombre et de son carré
            respect = True # Pour savoir si la propriété à été respecter pour un nombre
            
            if len(concatenation) == 9 :

                chiffres = set()

                for c in concatenation :

                    if c == '0' or c in chiffres : # Si le chiffre vaut 0 ou le chiffre était déjà présent
                        # ce nombre ne respecte pas la propriété
                        respect = False
                        break

                    else:
                        chiffres.add(c) # On ajoute ce chiffre dans notre ensemble

                # On vérifie si le nombre respect la proprité
                if respect:
                    return nombre

        # Cas contraire on continue la boucle en incrémentant le nombre
        nombre += 1

if __name__ == "__main__":
    print(currieux_chiffre_1_9())
