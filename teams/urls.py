from django.urls import path
from .views import TeamView, TeamViewParams

urlpatterns = [
    path('teams/', TeamView.as_view()),
    path('teams/<team_id>/', TeamViewParams.as_view())
]
