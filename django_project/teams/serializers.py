from rest_framework import serializers
from .models import Team
from players.serializers import PersonSerializer


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    members = PersonSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ['url', 'name', 'members']
        extra_kwargs = {
            'url': {'view_name': 'team-detail', 'lookup_field': 'pk'}
        }
