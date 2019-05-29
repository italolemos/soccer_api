from django.contrib import admin

from .models import Team, Player, Match, User


class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'abbreviation']
    prepopulated_fields = {'slug': ('name',), }


admin.site.register(Team, TeamAdmin)
admin.site.register(Player)
admin.site.register(Match)
admin.site.register(User)