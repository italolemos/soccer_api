from django.contrib import admin

from .models import Team, Player, Match, User, UserTeam, Scouts
from .forms import PlayerChoiceField


class ScoutsAdmin(admin.ModelAdmin):
    list_display = ['player', 'round']


class PlayerAdmin(admin.ModelAdmin):
    list_display = ['name', 'team', 'position', 'price']
    ordering = ['position']


class TeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'abbreviation']
    readonly_fields = ['slug']
    # prepopulated_fields = {'slug': ('name',), }


class UserTeamAdmin(admin.ModelAdmin):

    exclude = ['owner']
    list_display = ['team_name', 'owner']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "player1":
            return PlayerChoiceField(queryset=Player.objects.filter(position__iexact='GOL'))
        if db_field.name == "player2":
            return PlayerChoiceField(queryset=Player.objects.filter(position__iexact='LAT'))
        if db_field.name == "player3":
            return PlayerChoiceField(queryset=Player.objects.filter(position__iexact='LAT'))
        if db_field.name == "player4":
            return PlayerChoiceField(queryset=Player.objects.filter(position__iexact='ZAG'))
        if db_field.name == "player5":
            return PlayerChoiceField(queryset=Player.objects.filter(position__iexact='ZAG'))
        if db_field.name == "player6":
            return PlayerChoiceField(queryset=Player.objects.filter(position__iexact='MEI'))
        if db_field.name == "player7":
            return PlayerChoiceField(queryset=Player.objects.filter(position__iexact='MEI'))
        if db_field.name == "player8":
            return PlayerChoiceField(queryset=Player.objects.filter(position__iexact='MEI'))
        if db_field.name == "player9":
            return PlayerChoiceField(queryset=Player.objects.filter(position__iexact='ATA'))
        if db_field.name == "player10":
            return PlayerChoiceField(queryset=Player.objects.filter(position__iexact='ATA'))
        if db_field.name == "player11":
            return PlayerChoiceField(queryset=Player.objects.filter(position__iexact='ATA'))
        if db_field.name == "coach":
            kwargs["queryset"] = Player.objects.filter(position__iexact='TEC')
        return super(UserTeamAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.owner = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Team, TeamAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Match)
admin.site.register(User)
admin.site.register(Scouts, ScoutsAdmin)
admin.site.register(UserTeam, UserTeamAdmin)
