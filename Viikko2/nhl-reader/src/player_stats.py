class PlayerStats:

    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_players()

        filtered = [p for p in players if p.nationality == nationality]
        filtered.sort(key = lambda p: p.score, reverse=True)

        return filtered