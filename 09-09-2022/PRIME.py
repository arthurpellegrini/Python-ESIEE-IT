def est_premier(nombre: int) -> bool:
    """
    Cette fonction permet de déterminer si un nombre est premier.
    :param nombre: le nombre
    :return: soit True, soit False suivant respectivement si le nombre est premier ou non.
    """
    for i in range(2, nombre):
        if (nombre % i) == 0:
            return False
    return True


def algo_euclide(a: int, b: int) -> int:
    """
    Cette fonction permet le calcul du PGCD(Plus Grand Commun Diviseur) de deux nombres.
    :param a: un entier
    :param b: un entier
    :return: la valeur du PGCD
    """
    if b == 0:
        return a
    return algo_euclide(b, a % b)


def premier_entre_eux(a: int, b: int) -> bool:
    """
    Cette fonction permet de déterminer si deux nombres sont premiers entre eux à l'aide du PGCD.
    a et b sont premiers entre eux ssi PGCD(a, b) = 1.
    :param a: un entier
    :param b: un entier
    :return: un booléen qui est True si les nombres sont premiers entre eux et False sinon.
    """
    if algo_euclide(a, b) == 1:
        return True
    else:
        return False


def diviseurs(nombre: int) -> list:
    """
    Cette fonction permet de déterminer l'ensemble des diviseurs d'un nombre.
    :param nombre: nombre entier positif
    :return: une liste contenant tous les diviseurs du nombre
    """
    diviseurs = []
    for i in range(1, nombre + 1):
        if nombre % i == 0:
            diviseurs.append(i)
    return diviseurs


def nombre_amicaux(a: int, b: int) -> bool:
    """
    Cette fonction permet de faire la somme des diviseurs d'un nombre et de la comparer avec celle d'un autre.
    :param a: un entier positif
    :param b: un entier positif
    :return: True si amicaux et False sinon.
    """
    suma = 0
    sumb = 0
    for i in diviseurs(a):
        suma += i
    for j in diviseurs(b):
        sumb += j
    return suma == sumb


# --------------------------------MAIN--------------------------------#
if __name__ == '__main__':
    a = int(input("Donnez moi un nombre entier : "))
    b = int(input("Donnez moi un autre nombre entier : "))
    print("Le nombre %i est premier : " % a, est_premier(a))
    print("Le nombre %i est premier : " % b, est_premier(b))
    print("%i et %i sont premier entre eux : " % (a, b), premier_entre_eux(a, b))
    print("%i et %i sont amicaux : " % (a, b), nombre_amicaux(a, b))
