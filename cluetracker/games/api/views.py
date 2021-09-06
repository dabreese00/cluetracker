from rest_framework import viewsets, permissions
from games.models import (Game, Player, Card, PersonCard, WeaponCard, RoomCard,
                          Have, Pass, Show)
from games.api.serializers import (GameSerializer, PlayerSerializer,
                                   CardSerializer, PersonCardSerializer,
                                   WeaponCardSerializer, RoomCardSerializer,
                                   HaveSerializer, PassSerializer,
                                   ShowSerializer)


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


class PersonCardViewSet(viewsets.ModelViewSet):
    """API endpoints to allow viewing and editing PersonCards."""
    queryset = PersonCard.objects.all()
    serializer_class = PersonCardSerializer
    permissions_classes = [permissions.IsAuthenticated]


class WeaponCardViewSet(viewsets.ModelViewSet):
    """API endpoints to allow viewing and editing WeaponCards."""
    queryset = WeaponCard.objects.all()
    serializer_class = WeaponCardSerializer
    permissions_classes = [permissions.IsAuthenticated]


class RoomCardViewSet(viewsets.ModelViewSet):
    """API endpoints to allow viewing and editing RoomCards."""
    queryset = RoomCard.objects.all()
    serializer_class = RoomCardSerializer
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
