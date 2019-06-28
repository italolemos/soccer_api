from .models import Team, Player, UserTeam, Scouts
from rest_framework import serializers


class ScoutsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Scouts
        exclude = ['id']


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = '__all__'


class PlayerSerializer(serializers.ModelSerializer):
    team = TeamSerializer()

    class Meta:
        model = Player
        fields = '__all__'


class UserTeamSerializer(serializers.ModelSerializer):
    player1 = PlayerSerializer()
    player2 = PlayerSerializer()
    player3 = PlayerSerializer()
    player4 = PlayerSerializer()
    player5 = PlayerSerializer()
    player6 = PlayerSerializer()
    player7 = PlayerSerializer()
    player8 = PlayerSerializer()
    player9 = PlayerSerializer()
    player10 = PlayerSerializer()
    player11 = PlayerSerializer()
    coach = PlayerSerializer()

    class Meta:
        model = UserTeam
        exclude = ['id']
