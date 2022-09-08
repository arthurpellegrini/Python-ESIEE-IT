def calcul_imc(masse: float, taille: float) -> float:
    """
    Cette fonction permet le calcul de l'IMC d'une personne à l'aide de sa masse et de sa taille.
    :param masse: en kg
    :param taille: en m
    :return: la valeur de l'IMC
    """
    return masse / (taille ** 2)


if __name__ == '__main__':
    prenom = input("Veuillez entrez votre prénom : ")
    taille = float(input("Veuillez entrez votre taille(en m) : "))
    masse = float(input("Veuillez entrez votre masse corporelle(en kg) : "))
    print("Bonjour %s, votre IMC est de %.2f." % (prenom, calcul_imc(masse, taille)))
