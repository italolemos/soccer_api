from rest_framework import generics

from .models import Team, Player
from .serializers import TeamSerializer, PlayerSerializer


class TeamList(generics.ListAPIView):
    """
    List all teams.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamDetail(generics.RetrieveAPIView):
    """
    Retrieve a team.
    """
    lookup_field = 'pk'
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class PlayerDetail(generics.RetrieveAPIView):
    """
    Retrieve a player.
    """
    lookup_field = 'pk'
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

