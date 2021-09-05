from django.db import models


class Game(models.Model):
    """A single game of Clue, with associated game state.

    Game state is tracked from a single player's perspective, and includes the
    following:
        - a set of Players
        - a set of Cards
        - sets of known ClueRelations: Haves, Passes, and Shows

    By convention, Players and Cards sets will generally be constant and known
    from the start, while the sets of known ClueRelations will naturally
    change/grow through the course of the game.
    """

    created_timestamp = models.DateTimeField(auto_now_add=True)


class Player(models.Model):
    """A player in a single Game of Clue.

    A player has a name and an integer hand_size, as well as always belonging
    to a specific game.

    Player names are unique within a single Game.
    """

    name = models.CharField(max_length=255)
    hand_size = models.IntegerField()
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        related_name='players')

    class Meta:
        unique_together = ['name', 'game']


class Card(models.Model):
    """A card in a single Game of Clue.

    A Card has a name, as well as always belonging to a specific game.

    Card names are unique within a single game.
    """

    name = models.CharField(max_length=255)
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE)

    class Meta:
        unique_together = ['name', 'game']


class PersonCard(Card):
    """A person card in a single game of Clue."""
    pass


class WeaponCard(Card):
    """A weapon card in a single game of Clue."""
    pass


class RoomCard(Card):
    """A room card in a single game of Clue."""
    pass


class ClueRelation(models.Model):
    """A piece of knowledge that may indicate which Players have which Cards"""

    player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE)
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE)

    class Meta:
        abstract = True


class HavePass(ClueRelation):
    """An indication that a player has or does not have a given card."""

    card = models.ForeignKey(
        Card,
        on_delete=models.CASCADE)

    class Meta(ClueRelation.Meta):
        abstract = True


class Have(HavePass):
    """An indication that a player has a given card."""
    pass


class Pass(HavePass):
    """An indication that a player does not have a given card."""
    pass


class Show(ClueRelation):
    """An indication that a player has shown one of a set of 3 cards."""

    cards = models.ManyToManyField(Card)
