"""Script utilitaire pour créer un nouveau fichier problemX.py avec le bon format."""

import sys
import subprocess
from datetime import date

ENCODAGE = "utf-8"

def get_python_version():
    v = sys.version_info
    return f"{v.major}.{v.minor}.{v.micro}"

def create_problem(numero: int):
    filename = f"problem{numero}.py"

    try:
        open(filename, "x").close()
    except FileExistsError:
        print(f"Erreur : {filename} existe déjà.")
        sys.exit(1)

    today = date.today().strftime("%Y-%m-%d")
    python_version = get_python_version()

    template = f"""\
# -*- coding: {ENCODAGE} -*-
\"\"\"
Auteur : @bysalim
Création : {today}
Python : {python_version}
Encodage : {ENCODAGE.upper()}

Problème {numero} :
    
Version : V1.1
Durée environ : ... s
\"\"\"

from modules.timer import mesure_temps

# Idée :
#
#

@mesure_temps
def solution():
    \"\"\"\"\"\"
    pass

if __name__ == "__main__":
    print(solution())
"""

    with open(filename, "w", encoding=ENCODAGE) as f:
        f.write(template)

    print(f"{filename} créé avec succès.")

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage : python new_problem.py <numéro>")
        print("Exemple : python new_problem.py 42")
        sys.exit(1)

    create_problem(int(sys.argv[1]))
