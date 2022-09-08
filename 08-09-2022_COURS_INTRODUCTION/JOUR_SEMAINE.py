def jour_semaine(date: str) -> str:
    """
    Cette fonction permet de trouver le jour de la semaine à l'aide d'une date.
    :param date: la date pour laquelle on recherche le jour de la semaine.
    :return: le jour de la semaine correspondant à la date fournie en paramètre.
    """
    JOUR = ["Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]
    MOIS = {
        1 : 0,
        2 : 3,

    }
    nb = int(date.split("/")[2][2:])
    print(nb//4 + int(date.split("/")[0]))


if __name__ == '__main__':
    date = input("Donnez moi une date (au format JJ/MM/AAAA): ")
    print("Le %s était un %s" % (date, jour_semaine(date)))
