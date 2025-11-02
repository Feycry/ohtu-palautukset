import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_get_top_player(self):
        top_player = self.stats.top(1)[0]
        self.assertEqual(top_player.points, Player("Gretzky", "EDM", 35, 89).points)

    def test_find_player(self):
        player = self.stats.search("Kurri")

        self.assertEqual(player.points, Player("Kurri",   "EDM", 37, 53).points)

    def test_cannot_find_player(self):
        player = self.stats.search("Korhonen")

        self.assertEqual(player, None)

    def test_get_all_in_team(self):
        players = self.stats.team("EDM")

        self.assertEqual(len(players), 3)