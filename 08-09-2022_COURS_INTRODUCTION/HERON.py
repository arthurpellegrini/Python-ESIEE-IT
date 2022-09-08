def heron_sqrt(nombre: float, precision: int) -> float:
    """
    Cette fonction permet de calculer la racine carrée d'un nombre en utilisation la méthode de Héron.
    :return: la racine carrée du nombre donné en paramètres
    """
    an = 0
    a_init = nombre
    for i in range(precision):
        an = (a_init + (nombre / a_init)) / 2
        a_init = an
    return an


if __name__ == '__main__':
    nombre = float(input("La racine carrée de : "))
    precision = int(input("La précision de la racine carrée : "))
    print("La racine carrée de %f est %f" % (nombre, heron_sqrt(nombre, precision)))
