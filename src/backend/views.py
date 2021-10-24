from django.shortcuts import render

from backend.models import ExampleModel
from backend.serializers import ExampleSerializer
from rest_framework import mixins
from rest_framework import generics

# Create your views here.

# functions for getting ALL the objects from the database using GET method (that's where "List" comes from)
# and also for creating a new object using the POST method
class ExampleList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = ExampleModel.objects.all()
    serializer_class = ExampleSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# functions for getting info about a certain object from the database (by its primary key -> id) using GET method
# for updating an object using PUT method
# and for deleting an object using DELETE method
class ExampleIndividual(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = ExampleModel.objects.all()
    serializer_class = ExampleSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
