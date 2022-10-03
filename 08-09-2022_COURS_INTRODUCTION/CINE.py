def prix_place() -> float:
    """
    Cette fonction permet de déterminer le prix de la place de cinéma en fonction de l'âge et du status de la personne.
    Il faut aussi noter que le prix de la place n'est pas le même suivant si le film est en 3D ou non et si la personne
    possède déjà les lunettes pour cette technologie.
    :return: le prix de la place en €
    """
    prix = float(0)
    age = int(input("Quel âge avez-vous ? :"))

    if age < 18:
        if age < 14:
            prix += 5.00
        else:
            prix += 7.70
    else:
        if input("Êtes-vous étudiant ? (Y/N):") == "Y":
            prix += 8.70
        else:
            prix += 12.10

    if input("Le film est-il en 3D ? (Y/N):") == "Y":
        if input("Avez-vous des lunettes 3D? (Y/N):") == "Y":
            prix += 3.00
        else:
            prix += 2.00

    return prix


# --------------------------------MAIN--------------------------------#
if __name__ == '__main__':
    print("Vous devez payer %.2f €." % prix_place())
