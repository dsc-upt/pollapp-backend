from django.contrib import admin
from .models import ExampleModel, Option, Vote, Poll
# Register your models here.

admin.site.register(ExampleModel)
admin.site.register(Poll)
admin.site.register(Option)
admin.site.register(Vote)
