from rest_framework import serializers

from teams.models import Team
from .models import Person


class PersonSerializer(serializers.ModelSerializer):

    team = serializers.PrimaryKeyRelatedField(
        queryset=Team.objects.all(),
        required=False
    )

    class Meta:
        model = Person
        fields = ['url', 'first_name', 'last_name', 'email', 'team']
        extra_kwargs = {
            'url': {'view_name': 'person-detail', 'lookup_field': 'pk'}
        }

    def to_representation(self, instance):
        representation = super(PersonSerializer, self).to_representation(instance)
        representation['team'] = instance.team.name if instance.team else None
        return representation
