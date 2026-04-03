import time

def mesure_temps(func):
    def wrapper(*args, **kwargs):
        debut = time.time()
        resultat = func(*args, **kwargs)
        fin = time.time()
        duree = fin - debut
        print(f"⏱️  '{func.__name__}' exécutée en {duree:.4f} secondes")
        return resultat
    return wrapper