from .models import Team, Player
from rest_framework import serializers
from .models import User


class UserDisplaySerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username']


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = '__all__'


class PlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = '__all__'
