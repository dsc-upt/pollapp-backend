from django.db import models

# Create your models here.

class ExampleModel(models.Model):
    title = models.CharField(max_length = 64)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add = True)

class Poll(models.Model):
    title = models.CharField(max_length = 100)
    question = models.TextField(max_length = 500)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)