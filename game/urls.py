from django.urls import path

from .views import TeamList, TeamDetail, PlayerDetail, UserDisplayAPIView

app_name = 'game'
urlpatterns = [
    path('teams/', TeamList.as_view()),
    path('team/<int:pk>', TeamDetail.as_view()),
    path('player/<int:pk>', PlayerDetail.as_view()),
    path('user/', UserDisplayAPIView.as_view(), name="current-user")
]
