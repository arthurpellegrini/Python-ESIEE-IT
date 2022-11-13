class Personne:
    def __init__(self, nom: str, prenom: str):
        self.nom = nom
        self.prenom = prenom

    def get_nom(self) -> str:
        return self.nom

    def set_nom(self, nom: str) -> None:
        self.nom = nom

    def get_prenom(self) -> str:
        return self.prenom

    def set_prenom(self, prenom: str) -> None:
        self.prenom = prenom

    def __str__(self) -> str:
        return f"Personne[Nom:{self.nom},Prénom:{self.prenom}]"
