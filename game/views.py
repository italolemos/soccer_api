from django.views.generic.base import TemplateView
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Team, Player
from .serializers import TeamSerializer, PlayerSerializer, UserDisplaySerializer


class IndexTemplateView(TemplateView):

    def get_template_names(self):
        template_name = "index.html"
        return template_name


class UserDisplayAPIView(APIView):

    def get(self, request):
        serializer = UserDisplaySerializer(request.user)
        return Response(serializer.data)


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

