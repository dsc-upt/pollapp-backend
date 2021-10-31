from rest_framework import serializers
from backend.models import ExampleModel
from backend.models import Option
from backend.models import Vote


class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExampleModel
        fields = ('id', 'title', 'content', 'date')


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ('option', 'poll', 'voter', 'date')

        
class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ('id', 'content', 'poll')
