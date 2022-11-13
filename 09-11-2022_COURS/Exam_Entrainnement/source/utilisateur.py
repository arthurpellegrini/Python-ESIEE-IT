from .personne import Personne
from .compte import Compte


class Utilisateur(Personne):
    def __init__(self, nom: str, prenom: str, compte: Compte):
        super().__init__(nom, prenom)
        self.compte = compte

    def get_compte(self) -> Compte:
        return self.compte

    def set_compte(self, compte: Compte) -> None:
        self.compte = compte

    def __str__(self) -> str:
        return f"Utilisateur[{super().__str__()},{self.compte.__str__()}]"
