from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Team
from django.forms import model_to_dict


# Create your views here.
class TeamView(APIView):
    def post(self, request):
        team_data = request.data

        team = Team.objects.create(**team_data)

        return Response(model_to_dict(team), 201)

    def get(self, request):

        team_dict = [team for team in Team.objects.all().values()]

        return Response(team_dict)
