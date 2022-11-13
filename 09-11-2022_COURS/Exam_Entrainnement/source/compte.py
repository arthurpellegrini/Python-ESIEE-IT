class Compte:
    def __init__(self, login: str, mdp: str):
        self.login = login
        self.mdp = mdp

    def connexion(self) -> bool:
        with open("login.csv", "r", encoding='utf-8') as file:
            raw_lines = file.readlines()

        for raw_line in raw_lines:
            line = raw_line.split(";")
            if (self.login == line[0]) and (self.mdp == line[1]):
                return True
        return False

    def get_login(self) -> str:
        return self.login

    def set_login(self, login: str) -> None:
        self.login = login

    def get_mdp(self) -> str:
        return self.mdp

    def set_mdp(self, mdp: str) -> None:
        self.mdp = mdp

    def __str__(self) -> str:
        return f"Compte[{self.login}:{self.mdp}]"
