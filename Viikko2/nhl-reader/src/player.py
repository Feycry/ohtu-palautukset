class Player:
    def __init__(self, dic):
        self.name = dic['name']
        self.nationality = dic["nationality"]
        self.assists = dic["assists"]
        self.goals = dic["goals"]
        self.team = dic["team"]
        self.games = dic["games"]
        self.id = dic["id"]

    @property
    def score(self):
        return self.goals + self.assists

    def __str__(self):
        return f"{self.name} {self.team} {self.nationality} {self.score}"
