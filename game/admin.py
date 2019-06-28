from django.contrib import admin

from .models import Team, Player, Match, User, UserTeam, Scouts


class TeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'abbreviation']
    prepopulated_fields = {'slug': ('name',), }


class UserTeamAdmin(admin.ModelAdmin):
    list_display = ['team_name', 'owner']


admin.site.register(Team, TeamAdmin)
admin.site.register(Player)
admin.site.register(Match)
admin.site.register(User)
admin.site.register(Scouts)
admin.site.register(UserTeam, UserTeamAdmin)
