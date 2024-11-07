"""Code qui permet de trouver des nombres premiers."""
from math import sqrt

#### Fonction secondaire

def isprime(p):
    """Vérifie si le nombre passé en paramètre est un nombre premier
    Retourne un booléen"""
    n = int(sqrt(p))
    if p<=1:
        return False
    for i in range(2,n+1):
        if p%i==0:
            return False
    return True

print(isprime(97))

#### Fonction principale

def main():
    # vos appels à la fonction secondaire ici
    """Retourne la liste des nombres premiers en dessous de n"""
    for n in range(100):
        if isprime(n):
            print(n, end=", ")
    print()

if __name__ == "__main__":
    main()
