from rest_framework import serializers
from games.models import (Game, Player, Card, Have, Pass, Show)


class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ['url', 'id', 'created_timestamp']


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ['url', 'id', 'name', 'game', 'hand_size']


class CardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Card
        fields = ['url', 'id', 'name', 'kind', 'game']


class HaveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Have
        fields = ['url', 'id', 'game', 'player', 'card']


class PassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pass
        fields = ['url', 'id', 'game', 'player', 'card']


class ShowSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Show
        fields = ['url', 'id', 'game', 'player', 'person', 'weapon', 'room']
