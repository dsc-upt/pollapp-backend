from rest_framework import serializers
from backend.models import ExampleModel
from backend.models import Option

class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExampleModel
        fields = ('id', 'title', 'content', 'date')


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ('id', 'content', 'poll')
