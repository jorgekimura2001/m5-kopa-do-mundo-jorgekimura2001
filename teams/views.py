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


class TeamViewParams(APIView):
    def get(self, request, team_id):
        try:
            team = Team.objects.get(pk=team_id)
            team_dict = model_to_dict(team)
            return Response(team_dict)

        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, 404)

    def delete(self, request, team_id):
        try:
            Team.objects.get(pk=team_id).delete()
            return Response(None, 204)

        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, 404)

    def patch(self, request, team_id):
        try:
            team = Team.objects.get(pk=team_id)

            for key, value in request.data.items():
                setattr(team, key, value)
            team.save()
            return Response(model_to_dict(team))

        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, 404)
