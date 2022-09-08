def syracuse(n: int, N: int) -> list:
    """
    Cette fonction permet en partant d'un entier supérieur à 0 de renvoyer une suite de Syracuse.
    :param n: un entier supérieur à 0
    :param N: le nombre de récursions
    :return: list
    """
    tab = [n]
    if n > 0:
        for i in range(N + 1):
            if n % 2 == 0:
                n = n / 2
            else:
                n = n * 3 + 1
            tab.append(int(n))
    return tab


def cycle_syracuse(n: int) -> str:
    """
    Cette fonction permet de savoir si la suite qui part de ce nombre tombe sur 4 ou 1 et ainsi de déterminer si ce
    nombre est respectivement malheureux ou heureux.
    :param n: un entier supérieur à 0
    :return: une chaîne de caractères qui affiche soit 'heureux' soit 'malheureux'.
    """
    if n > 0:
        while True:
            total = 0
            for i in str(n):
                total += int(i) ** 2
            n = total
            if n == 4:
                return "malheureux"
            if n == 1:
                return "heureux"
    return ""


if __name__ == '__main__':
    n = int(input("Un entier supérieur à 0 : "))
    N = int(input("La taille de la suite de syracuse : "))
    print("Voici la suite de syracuse générée : ", syracuse(n, N))
    print("Ce nombre est un nombre %s" % cycle_syracuse(n))
