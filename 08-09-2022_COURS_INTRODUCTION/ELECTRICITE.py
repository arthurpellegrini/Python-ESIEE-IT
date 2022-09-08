def programme(conso: float) -> str:
    """
    Cette fonction permet de déterminer le programme le plus adéquat en fonction de la consommation du client
    :param conso: la consommation du client
    :return: une chaîne de caractères contenant le programme correspondant
    """
    if conso < 3:
        return "5,74€/mois + 15,55€/KWh"
    elif conso < 6:
        return "8,92€/mois + 14,67€/KWh"
    elif conso < 9:
        return "10,42€/mois + 14,83€/KWh"
    elif conso < 12:
        return "11,96€/mois + 14,83€/KWh"
    elif conso < 15:
        return "13,50€/mois + 14,83€/KWh"


if __name__ == '__main__':
    conso = float(input("Combien consommez-vous ? : "))
    print("Le prix de l'abonnement sera de %s" % programme(conso))
