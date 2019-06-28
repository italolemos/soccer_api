from django.http import HttpResponse
from rest_framework import generics

from .models import Team, Player, UserTeam, Scouts
from .serializers import TeamSerializer, PlayerSerializer, UserTeamSerializer, ScoutsSerializer


class ScoutPlayerDetail(generics.RetrieveAPIView):
    """
    Scout a player detail.
    """
    lookup_field = 'pk'
    queryset = Scouts.objects.all()
    serializer_class = ScoutsSerializer


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


class PlayerList(generics.ListAPIView):
    """
    List all playeres.
    """
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class UserTeamDetail(generics.ListAPIView):
    """
    Retrieve a user team.
    """
    lookup_field = 'pk'
    queryset = UserTeam.objects.all()
    serializer_class = UserTeamSerializer


def importar_clubs(self):
    clubes = [
        ['América-MG', 'AMG', 'america-mg'],
        ['Atlético-GO', 'ATL', 'atletico'],
        ['Botafogo-SP', 'BTF', 'botafogo-sp'],
        ['Bragantino', 'BGR', 'bragantino'],
        ['Brasil de Pelotas', 'BPL', 'brasil-pelotas'],
        ['Coritiba', 'COR', 'coritiba'],
        ['Criciúma', 'CRI', 'criciuma'],
        ['CRB', 'CRB', 'crb'],
        ['Cuiabá', 'CUB', 'cuiaba'],
        ['Figueirense', 'FIG', 'figueirense'],
        ['Guarani', 'GUA', 'guarani'],
        ['Londrina', 'LON', 'londrina'],
        ['Oeste', 'OES', 'oeste'],
        ['Operário-PR', 'OPE', 'operario-pr'],
        ['Paraná', 'PAR', 'parana'],
        ['Ponte Preta', 'PON', 'ponte-preta'],
        ['São Bento', 'SAB', 'sao-bento'],
        ['Sport', 'SPO', 'sport'],
        ['Vila Nova', 'VIL', 'vila-nova'],
        ['Vitória', 'VIT', 'vitoria']
    ]

    for c in clubes:
        Team.objects.update_or_create(name=c[0],
                                      abbreviation=c[1],
                                      slug=c[2])
    return HttpResponse('OK')


def importar_atletas(self):
    atletas = [
        ['Mailson', 'mailson', 18, 'GOL', 8.00],
        ['Michel Bastos', 'michel-bastos', 1, 'MEI', 12.00],
        ['Hernane', 'hernane', 18, 'ATA', 9.00],
        ['Sander', 'sander', 18, 'LAT', 5.00],
        ['Paulão', 'paulao', 16, 'ZAG', 2.00]

    ]

    for a in atletas:
        Player.objects.update_or_create(name=a[0],
                                        slug=a[1],
                                        team=Team.objects.get(id=a[2]),
                                        position=a[3],
                                        price=a[4])
    return HttpResponse('OK')
