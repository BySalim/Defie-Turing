# -*- coding: utf-8 -*-
"""
Auteur : @bysalim
Création : 2026-04-05
Python : 3.14.3
Encodage : UTF-8

Problème 19 :
    Des petits hommes verts rencontrent des petits hommes bleus.
    A leur grand étonnement, ils constatent que leurs mains ne comportent pas le même nombre de doigts : 
    7 pour les bleus et 8 pour les verts.
    Mais les savants des deux peuples remarquent que si l'on compte sur les doigts comme indiqué sur la figure, 
    en faisant des allers-retours de l'auriculaire vers le pouce, puis du pouce vers l'auriculaire, 
    certains nombres se comptent à la fois sur l'annulaire des mains bleues 
    et sur celui des mains vertes (le 2 et le 14 par exemple).
    Ces nombres ont été qualifiés d'"annulaires" par les savants.
    Calculer la somme des nombres annulaires compris entre 1 et 2013.
Version : V1.1
Durée environ : 0.0001 s
"""

from modules.timer import mesure_temps

# Idée : 
# annulaires mains une (7) : 2 12 14 24 26 36 : On remarque également que si le tour est impaire on ajoute 2 et dans le cas contraire on ajoute 10 donc la période est 10 + 2 = 12
# annulaires main deux (8) : 2 14 16 28 30 42 : On remarque que si le tour est impaire on ajoute 2 à l'ancienne valeur et si le tour est paire on ajoute 12 donc la péroide est 14 + 2 = 14

def periode(nb_doigts):
    """Calcul la péroide à partir du nombre de doigts d'une main"""
    return 2*(nb_doigts-1)

def annulaires_main(periode, fin):
    """Liste les annulaires inférieur à [fin] d'une main à partir de sa [periode]"""
    positions = set()
    # Premier annulaire = 2, puis alterne +2 et +(periode-2)
    val = 2
    while val <= fin:
        positions.add(val)
        val += periode - 2   # ex: +10 pour bleu, +12 pour vert
        if val <= fin:
            positions.add(val)
        val += 2
    return positions

@mesure_temps
def somme_nombres_annulaires(debut, fin):
    # Nombres de doigts
    DOIGTS_BLEUS = 7
    DOIGTS_VERTS = 8
    
    # Péroide de chaque main
    PERIODE_BLEU = periode(DOIGTS_BLEUS)
    PERIODE_VERT = periode(DOIGTS_VERTS)

    # Annulaires de chaque main jusqu'à fin
    Main_bleu = annulaires_main(PERIODE_BLEU, fin)
    Main_vert = annulaires_main(PERIODE_VERT, fin)

    # L'intersection des deux ensembles nous donne les annulaires
    Annulaires = Main_bleu & Main_vert

    # Filtrer et sommer dans [debut, fin]. [fin] déjà pris en compte dans annulaires_main
    return sum(x for x in Annulaires if debut <= x)
    
if __name__ == "__main__":
    print(somme_nombres_annulaires(1,2013))
    
    