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
        ['América-MG', 'AMG'],
        ['Atlético-GO', 'ATL'],
        ['Botafogo-SP', 'BTF'],
        ['Bragantino', 'BGR'],
        ['Brasil de Pelotas', 'BPL'],
        ['Coritiba', 'COR'],
        ['Criciúma', 'CRI'],
        ['CRB', 'CRB', 'crb'],
        ['Cuiabá', 'CUB'],
        ['Figueirense', 'FIG'],
        ['Guarani', 'GUA'],
        ['Londrina', 'LON'],
        ['Oeste', 'OES'],
        ['Operário-PR', 'OPE'],
        ['Paraná', 'PAR'],
        ['Ponte Preta', 'PON'],
        ['São Bento', 'SAB'],
        ['Sport', 'SPO'],
        ['Vila Nova', 'VIL'],
        ['Vitória', 'VIT']
    ]

    for c in clubes:
        Team.objects.update_or_create(name=c[0],
                                      abbreviation=c[1],
                                      )
    return HttpResponse('OK')


def importar_atletas(self):
    atletas = [
        ['Mailson', 'SPO', 'GOL', 8.00],
        ['Michel Bastos', 'AMG', 'MEI', 12.00],
        ['Hernane', 'SPO', 'ATA', 9.00],
        ['Sander', 'SPO', 'LAT', 5.00],
        ['Paulão', 'SPO', 'ZAG', 2.00],
        ['Alex Muralha', 'COR', 'GOL', 4.00],
        ['Rodrigão', 'COR', 'ATA', 6.00],
        ['Victor Ramos', 'CRB', 'ZAG', 4.50],
        ['Marcelo Chamusca', 'CRB', 'TEC', 2.00],
        ['Roger', 'PON', 'ATA', 7.00],
        ['Doriva', 'PON', 'TEC', 5.00],
        ['Luan Sales', 'ATL', 'LAT', 4.00]
    ]

    for a in atletas:
        Player.objects.update_or_create(name=a[0],
                                        team=Team.objects.get(abbreviation=a[1]),
                                        position=a[2],
                                        price=a[3])
    return HttpResponse('OK')
