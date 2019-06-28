from django.urls import path

from .views import TeamList, TeamDetail, PlayerDetail, UserTeamDetail, ScoutPlayerDetail,\
    importar_clubs, importar_atletas, PlayerList

app_name = 'game'
urlpatterns = [
    path('clubs/', TeamList.as_view()),
    path('club/<int:pk>', TeamDetail.as_view()),
    path('players/', PlayerList.as_view()),
    path('player/<int:pk>', PlayerDetail.as_view()),
    path('team/<int:pk>', UserTeamDetail.as_view()),
    path('pontuacao/<int:pk>', ScoutPlayerDetail.as_view()),

    #Imports
    path('importar_clubes/', importar_clubs),
    path('importar_atletas/', importar_atletas),
]
