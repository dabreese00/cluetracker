from django.test import TestCase
from games.models import Game, Player
from django.db import IntegrityError


class PlayerTestCase(TestCase):

    def setUp(self):
        g = Game.objects.create()
        Player.objects.create(name="Bob", hand_size=3, game=g)

    def test_player_names_are_unique(self):
        """Cannot add two Players with the same name to a single Game."""
        g = Game.objects.first()

        with self.assertRaises(IntegrityError):
            Player.objects.create(name="Bob", hand_size=4, game=g)
