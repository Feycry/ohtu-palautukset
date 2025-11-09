import requests
from player import Player

class PlayerReader:

    def __init__(self, url: str):
        self.url = url
        self.json = requests.get(url, timeout=10).json()

    def get_players(self):
        players = []

        for player_dict in self.json:
            player = Player(player_dict)
            players.append(player)

        return players
