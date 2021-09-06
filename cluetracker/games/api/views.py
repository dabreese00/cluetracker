from rest_framework import viewsets, permissions
from games.models import (Game, Player, Card, Have, Pass, Show)
from games.api.serializers import (GameSerializer, PlayerSerializer,
                                   CardSerializer, HaveSerializer,
                                   PassSerializer, ShowSerializer)


class GameViewSet(viewsets.ModelViewSet):
    """API endpoints to allow viewing and editing games."""
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permissions_classes = [permissions.IsAuthenticated]


class PlayerViewSet(viewsets.ModelViewSet):
    """API endpoints to allow viewing and editing players."""
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permissions_classes = [permissions.IsAuthenticated]


class CardViewSet(viewsets.ModelViewSet):
    """API endpoints to allow viewing and editing cards."""
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permissions_classes = [permissions.IsAuthenticated]


class HaveViewSet(viewsets.ModelViewSet):
    """API endpoints to allow viewing and editing Haves."""
    queryset = Have.objects.all()
    serializer_class = HaveSerializer
    permissions_classes = [permissions.IsAuthenticated]


class PassViewSet(viewsets.ModelViewSet):
    """API endpoints to allow viewing and editing Passes."""
    queryset = Pass.objects.all()
    serializer_class = PassSerializer
    permissions_classes = [permissions.IsAuthenticated]


class ShowViewSet(viewsets.ModelViewSet):
    """API endpoints to allow viewing and editing Shows."""
    queryset = Show.objects.all()
    serializer_class = ShowSerializer
    permissions_classes = [permissions.IsAuthenticated]
