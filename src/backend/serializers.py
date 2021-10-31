from rest_framework import serializers
from backend.models import ExampleModel, Vote


class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExampleModel
        fields = ('id', 'title', 'content', 'date')


class Vote(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ('option', 'poll', 'voter', 'date')