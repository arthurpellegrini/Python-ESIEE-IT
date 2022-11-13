from source import *

if __name__ == "__main__":
    personne = Personne("Pellegrini", "Arthur")
    compte = Compte("apellegr", "azerty")
    utilisateur = Utilisateur("Pellegrini", "Arthur", compte)
    print("LOGIN/MDP : ", utilisateur.compte.connexion())

    artiste1 = Artiste("1", "Michel", "Olympia")

    artiste2 = Artiste("2", "Michel", "Olympia")

    # artiste2 = Artiste(input("Entrer le nom de l'artiste : "),
    #                    input("Entrer le prenom d'artiste : "),
    #                    input("Entrer le nom de la scène : "))

    spectacle1 = Spectacle("titre", "13/11/2022", 45.99, 150)
    spectacle1.add_artiste(artiste1)
    spectacle1.add_artiste(artiste2)

    spectacle2 = Spectacle("titre", "13/11/2022", 95.99, 150)
    spectacle2.add_artiste(Artiste("Grand", "Michel", "Olympia"))
    spectacle2.add_artiste(Artiste("Dépêche", "Michel", "Grand Rex"))
    spectacle2.add_artiste(Artiste("François", "Michel", "Palais des Glaces"))
    # spectacle2.add_artiste(Artiste("2", "Michel", "Olympia"))

    print("NB Artistes", spectacle1.nb_artistes(), spectacle2.nb_artistes())
    print("Artiste en communs : ", spectacle1.has_commun_artiste(spectacle2))

    programmation = Programmation()
    programmation.add_spectacle(spectacle1)
    programmation.add_spectacle(spectacle2)

    print("Spectacles en fonction du prix max")
    tab_spectacles_correspondants = programmation.select_prix(46)
    for spectacle in tab_spectacles_correspondants:
        print(spectacle)

    print("Spectacles en fonction d'un artiste")
    tab_spectacles_correspondants = programmation.select_artiste(Artiste("Grand", "Michel", "Olympia"))
    for spectacle in tab_spectacles_correspondants:
        print(spectacle)

    # print("Spectacles en fonction de plusieurs artistes")
    # tab_spectacles_correspondants = programmation.select_artistes([Artiste("Grand", "Michel", "Olympia"),
    #                                                                Artiste("Grand", "Gilbert", "JSP")])
    # for spectacle in tab_spectacles_correspondants:
    #     print(spectacle)

    print("PRIX MOYEN : ", programmation.prix_moyen())
    # print("ALL_MAX_SPECTACLES : ", programmation.allMaxSpectacles())
    programmation.saveToJson("sav_13-11-2022.json")

    # TODO: Ajouter Lecture XML
