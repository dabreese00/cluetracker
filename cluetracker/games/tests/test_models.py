from django.test import TestCase
from games.models import Game, Player, Card, Have, Pass, Show
from django.db import IntegrityError


class GameTestCase(TestCase):

    def setUp(self):

        self.game = Game.objects.create()
        self.player = Player.objects.create(
            name="Bob",
            hand_size=3,
            game=self.game
        )
        self.personcard = Card.objects.create(
            name="Colonel Mustard",
            kind=Card.PERSON,
            game=self.game
        )
        self.weaponcard = Card.objects.create(
            name="Rope",
            kind=Card.WEAPON,
            game=self.game
        )
        self.roomcard = Card.objects.create(
            name="Billiard Room",
            kind=Card.ROOM,
            game=self.game
        )

    def test_add_single_player(self):
        player1 = Player.objects.create(
            name="Alice",
            hand_size=3,
            game=self.game
        )
        self.assertEqual(self.game.players.get(name="Alice"), player1)

    def test_add_single_card(self):
        card1 = Card.objects.create(
            name="Ballroom",
            kind=Card.ROOM,
            game=self.game
        )
        self.assertEqual(self.game.cards.get(name="Ballroom"), card1)

    def test_add_single_have(self):
        have1 = Have.objects.create(
            player=self.player,
            card=self.personcard,
            game=self.game
        )
        self.assertEqual(
            self.game.haves.get(player=self.player),
            have1
        )

    def test_add_single_pass(self):
        pass1 = Pass.objects.create(
            player=self.player,
            card=self.weaponcard,
            game=self.game
        )
        self.assertEqual(
            self.game.passes.get(player=self.player),
            pass1
        )

    def test_add_single_show(self):
        show1 = Show.objects.create(
            player=self.player,
            person=self.personcard,
            weapon=self.weaponcard,
            room=self.roomcard,
            game=self.game
        )
        self.assertEqual(
            self.game.shows.get(player=self.player),
            show1
        )


class PlayerTestCase(TestCase):

    def setUp(self):

        self.game = Game.objects.create()
        self.player = Player.objects.create(
            name="Bob",
            hand_size=3,
            game=self.game
        )

    def test_player_names_are_unique(self):
        """
        Cannot add two Players with the same name to a single Game.
        """
        with self.assertRaises(IntegrityError):
            Player.objects.create(
                name="Bob",  # duplicate name
                hand_size=4,
                game=self.game
            )

    def test_create_same_player_new_game(self):
        """
        Can add a 2nd player with the same name to a different Game.
        """
        game2 = Game.objects.create()
        player2 = Player.objects.create(
            name="Bob",  # duplicate name
            hand_size=3,
            game=game2
        )
        self.assertTrue(player2)


class CardTestCase(TestCase):

    def setUp(self):

        self.game = Game.objects.create()
        self.card = Card.objects.create(
            name="Colonel Mustard",
            kind=Card.PERSON,
            game=self.game
        )

    def test_card_types_are_defined(self):
        """
        Card types should be PERSON, WEAPON, ROOM.
        """
        self.assertTrue(Card.PERSON)
        self.assertTrue(Card.WEAPON)
        self.assertTrue(Card.ROOM)

    def test_card_names_are_unique(self):
        """
        Cannot add two Cards with the same name to a single Game.
        """
        with self.assertRaises(IntegrityError):
            Card.objects.create(
                name="Colonel Mustard",
                kind=Card.WEAPON,
                game=self.game
            )

    def test_create_same_card_new_game(self):
        """
        Can add a 2nd card with the same name to a different game.
        """
        game2 = Game.objects.create()
        card2 = Card.objects.create(
            name="Colonel Mustard",
            kind=Card.PERSON,
            game=game2
        )

        self.assertTrue(card2)
