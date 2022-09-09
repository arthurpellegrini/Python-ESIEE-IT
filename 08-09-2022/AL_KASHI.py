import math


def calcul_distance(a: float, b: float, gamma: float) -> float:
    """
    Cette fonction permet le calcul de la longueur d'un côté d'un triangle à l'aide des deux autres côtés ainsi que de
    leur angle.
    :param a: la longueur d'un côté du triangle
    :param b: la longueur d'un autre côté du triangle
    :param gamma: la valeur de l'angle entre les côtés a et b
    :return: la longueur du dernier côté du triangle
    """
    return math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(math.radians(gamma)))


def calcul_angle(a: float, b: float, c: float) -> float:
    """
    Cette fonction permet le calcul d'un angle d'un triangle quelconque à partir des côtés de celui-ci. Le premier
    paramètre correspondra à l'angle recherché.
    :param a: la longueur d'un côté du triangle
    :param b: la longueur d'un côté du triangle
    :param c: la longueur d'un côté du triangle
    :return: la valeur de l'angle recherché
    """
    return math.degrees(math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)))


# --------------------------------MAIN--------------------------------#
if __name__ == '__main__':
    a = float(input("Donnez une valeur pour a : "))
    b = float(input("Donnez une valeur pour b : "))
    gamma = float(input("Donnez une valeur pour gamma : "))

    c = calcul_distance(a, b, gamma)
    alpha = calcul_angle(a, b, c)
    beta = calcul_angle(b, a, c)

    print("c = %.5f" % c)
    print("alpha  = %.5f" % alpha)
    print("beta = %.5f" % beta)
