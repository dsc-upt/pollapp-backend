from django.shortcuts import render

from backend.models import ExampleModel
from backend.models import Vote
from backend.models import Poll
from backend.models import Option
from backend.serializers import ExampleSerializer
from backend.serializers import OptionSerializer
from backend.serializers import PollSerializer
from backend.serializers import VoteSerializer
from rest_framework import mixins
from rest_framework import generics


# Create your views here.

class ExampleList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = ExampleModel.objects.all()
    serializer_class = ExampleSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ExampleIndividual(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = ExampleModel.objects.all()
    serializer_class = ExampleSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class OptionList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class OptionIndividual(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class VoteList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class VoteIndividual(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class PollList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class PollIndividual(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)