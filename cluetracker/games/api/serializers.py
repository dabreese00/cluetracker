from rest_framework import serializers
from games.models import (Game, Player, Card, Have, Pass, Show)


class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ['url', 'id', 'created_timestamp']


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ['url', 'name', 'game', 'hand_size']


class CardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Card
        fields = ['url', 'name', 'kind', 'game']


class HaveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Have
        fields = ['url', 'game', 'player', 'card']


class PassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pass
        fields = ['url', 'game', 'player', 'card']


class ShowSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Show
        fields = ['url', 'game', 'player', 'person', 'weapon', 'room']
