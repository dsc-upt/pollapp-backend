from rest_framework import serializers
from backend.models import ExampleModel

class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExampleModel
        fields = ('id', 'title', 'content', 'date')