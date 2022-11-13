def read_file(debit: int) -> float:
    """
    Cette fonction permet la lecture à une ligne précise du fichier afin de déterminer la différence de pression(Pa)
    sur un debit.
    :param debit:
    :return: la différence de pression sur le débit fourni en paramètres
    """
    with open("Courbe ventilo.txt", "r") as file:
        debits = file.read().split("\n")[debit - 1].split(",")
    return float(debits[1]) - float(debits[0])


# --------------------------------MAIN--------------------------------#
if __name__ == '__main__':
    ligne = int(input("Quel débit voulez-vous tester ? : "))
    print("La différence de pression sur le débit %i est de %0.2f Pa" % (ligne, read_file(ligne)))
