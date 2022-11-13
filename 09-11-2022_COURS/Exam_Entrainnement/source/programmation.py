import json

from .artiste import Artiste
from .spectacle import Spectacle


class Programmation:
    def __init__(self):
        self.spectacles = []

    def get_spectacles(self) -> list:
        return self.spectacles

    def add_spectacle(self, spectacle: Spectacle) -> None:
        self.spectacles.append(spectacle)

    def select_prix(self, prix_max: float) -> list:
        spectacles_correspondants = []
        for spectacle in self.spectacles:
            if spectacle.prix <= prix_max:
                spectacles_correspondants.append(spectacle)
        return spectacles_correspondants

    def select_artiste(self, par_artiste: Artiste) -> list:
        spectacles_correspondants = []
        for spectacle in self.spectacles:
            for artiste in spectacle.artistes:
                if artiste.__eq__(par_artiste):
                    spectacles_correspondants.append(spectacle)
        return spectacles_correspondants

    def select_artistes(self, par_artistes: list) -> list:
        spectacles_correspondants = []
        for spectacle in self.spectacles:
            if par_artistes in spectacle.artistes:
                spectacles_correspondants.append(spectacle)
        return spectacles_correspondants

    def prix_moyen(self) -> float:
        prix = 0
        for spectacle in self.spectacles:
            prix += spectacle.prix
        return prix / len(self.spectacles)

    def allMaxSpectacles(self):
        # TODO
        pass

    def saveToJson(self, filename: str) -> None:
        programmation = []
        for spectacle in self.spectacles:
            programmation.append(spectacle.to_json_dict())

        with open(filename, "w", encoding='utf-8') as file:
            file.write(json.dumps(programmation, indent=4, ensure_ascii=False))

    def __str__(self) -> str:
        output = ""
        for spectacle in self.spectacles:
            output = spectacle.__str__()
        return f"Programmation[{output}]"
