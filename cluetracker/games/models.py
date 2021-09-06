from django.db import models


class Game(models.Model):
    """A single game of Clue, with associated game state.

    Game state is tracked from a single player's perspective, and includes the
    following, by relation:
        - players: a set of Players
        - cards: a set of Cards
        - haves: a set of ClueRelations
        - passes: a set of ClueRelations
        - shows: a set of ClueRelations
    """

    created_timestamp = models.DateTimeField(
        auto_now_add=True
    )


class Player(models.Model):
    """A player in a single Game of Clue.

    A player has:
        - name: a string
        - hand_size: an integer indicating how many cards Player holds
        - game: the Game to which the player belongs

    Player names are unique within a single Game.
    """

    name = models.CharField(
        max_length=255
    )
    hand_size = models.IntegerField()
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        related_name='players'
    )

    class Meta:
        unique_together = ['name', 'game']


class Card(models.Model):
    """A card in a single Game of Clue.

    The Card class enumerates three possible card types:
        - Card.PERSON
        - Card.WEAPON
        - Card.ROOM

    A Card instance has:
        - name: a string
        - kind: one of the card types defined in this class
        - game: the Game to which the card belongs

    Card names are unique within a single game.
    """

    PERSON = 'P'
    WEAPON = 'W'
    ROOM = 'R'

    CARD_TYPE_CHOICES = [
        (PERSON, 'Person'),
        (WEAPON, 'Weapon'),
        (ROOM, 'Room'),
    ]

    name = models.CharField(
        max_length=255
    )
    kind = models.CharField(
        max_length=1,
        choices=CARD_TYPE_CHOICES
    )
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        related_name='cards'
    )

    class Meta:
        unique_together = ['name', 'game']


class Have(models.Model):
    """An indication that a player has a given card."""
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        related_name='haves'
    )
    player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        related_name='haves'
    )
    card = models.ForeignKey(
        Card,
        on_delete=models.CASCADE,
        related_name='haves'
    )


class Pass(models.Model):
    """An indication that a player does not have a given card.

    Note, contrary to the common use of the word "Pass" in a Clue game, here a
    Pass need not indicate that the specified player actually verbally "passed"
    on the specified card, in the game; instead, for simplicity, we are
    overloading the term here to apply to any situation in which we come to
    know that the specified player does not hold the specified card.
    """
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        related_name='passes'
    )
    player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        related_name='passes'
    )
    card = models.ForeignKey(
        Card,
        on_delete=models.CASCADE,
        related_name='passes'
    )


class Show(models.Model):
    """An indication that a player has shown one of a set of 3 cards.

    person - the Person Card that was possibly shown
    weapon - the Weapon Card that was possibly shown
    room - the Room Card that was possibly shown
    """

    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        related_name='shows'
    )
    player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        related_name='shows'
    )
    person = models.ForeignKey(
        Card,
        on_delete=models.CASCADE,
        related_name='person_shows'
    )
    weapon = models.ForeignKey(
        Card,
        on_delete=models.CASCADE,
        related_name='weapon_shows'
    )
    room = models.ForeignKey(
        Card,
        on_delete=models.CASCADE,
        related_name='room_shows'
    )
