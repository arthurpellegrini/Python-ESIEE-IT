from .personne import Personne


class Inscrit:
    def __init__(self):
        self.personnes = []

    def get_personnes(self) -> list:
        return self.personnes

    def add_personne(self, personne: Personne) -> None:
        self.personnes.append(personne)

    def __str__(self) -> str:
        output = ""
        for personne in self.personnes:
            output += personne.__str__()
        return f"Inscrit[{output}]"
