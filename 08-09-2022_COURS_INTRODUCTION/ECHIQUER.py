def jeu_echec() -> float:
    """
    INTRODUCTION :
    La légende raconte qu’un jour, un roi découvrit un nouveau jeu : le jeu d’échec. Le concepteur du jeu voulu que le
    roi pose un grain de riz sur la première case du jeu et double le nombre de grains de riz à chaque case.

    Cette fonction va donc permettre de stocker le nombre de grains de riz une fois la 64e case du plateau atteinte.
    :return: le nombre de tonnes de grains de riz à la fin du jeu.
    """
    tab = []
    riz = 1
    for i in range(0, 64):
        tab.append(riz)
        riz = riz * 2

    return float(tab[-1] * 2 * 10 ** (-8))


# --------------------------------MAIN--------------------------------#
if __name__ == '__main__':
    print("La masse de la totalité des grains riz est de %.8f tonnes." % jeu_echec())
