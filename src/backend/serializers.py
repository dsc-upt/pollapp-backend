from rest_framework import serializers
from backend.models import ExampleModel

class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExampleModel
        fields = ('id', 'title', 'content', 'date')

class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollModel
        fields = ('id', 'title', 'question', 'creator')