from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ExampleModel(models.Model):
    title = models.CharField(max_length=64)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


class Poll(models.Model):
    title = models.CharField(max_length = 100)
    question = models.TextField(max_length = 500)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)


class Option(models.Model):
    content = models.TextField()
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)


class Vote(models.Model):
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)