from typing import Self
from .personne import Personne


class Artiste(Personne):
    def __init__(self, nom: str, prenom: str, nom_scene: str):
        super().__init__(nom, prenom)
        self.nom_scene = nom_scene

    def get_nom_scene(self) -> str:
        return self.nom_scene

    def set_nom_scene(self, nom_scene: str) -> None:
        self.nom_scene = nom_scene

    def __eq__(self, artiste: Self) -> bool:
        if(self.nom == artiste.nom) and (self.prenom == artiste.prenom) and (self.nom_scene == artiste.nom_scene):
            return True
        return False

    def __str__(self) -> str:
        return f"Artiste[{super().__str__()},NomScène:{self.nom_scene}]"
