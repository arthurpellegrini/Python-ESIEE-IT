from typing import Self

from .artiste import Artiste


class Spectacle:
    def __init__(self, titre: str, date: str, prix: float, nb_places: int):
        self.titre = titre
        self.date = date
        self.prix = prix
        self.nb_places = nb_places
        self.artistes = []

    def add_artiste(self, artiste: Artiste) -> None:
        self.artistes.append(artiste)

    def nb_artistes(self) -> int:
        return len(self.artistes)

    def has_commun_artiste(self, spectacle: Self) -> bool:
        for artiste1 in spectacle.artistes:
            for artiste2 in self.artistes:
                if artiste1.__eq__(artiste2):
                    return True
        return False

    def get_titre(self) -> str:
        return self.titre

    def set_titre(self, titre: str) -> None:
        self.titre = titre

    def get_date(self) -> str:
        return self.date

    def set_date(self, date: str) -> None:
        self.date = date

    def get_prix(self) -> float:
        return self.prix

    def set_prix(self, prix: float) -> None:
        self.prix = prix

    def get_nb_places(self) -> int:
        return self.nb_places

    def set_nb_places(self, nb_places: int) -> None:
        self.nb_places = nb_places

    def to_json_dict(self) -> dict:
        liste_artistes = []
        for artiste in self.artistes:
            liste_artistes.append(artiste.__str__())
        return {
            "TITRE": self.titre,
            "DATE": self.date,
            "PRIX": self.prix,
            "NB_PLACES": self.nb_places,
            "ARTISTES": liste_artistes
        }

    def __str__(self) -> str:
        output_artiste = ""
        for artiste in self.artistes:
            output_artiste += artiste.__str__()
        return f"Spectacle[Titre:{self.titre},Date:{self.date},Prix:{self.prix}€,NbPlaces:{self.nb_places}," \
               f"Artistes[{output_artiste}]]"
