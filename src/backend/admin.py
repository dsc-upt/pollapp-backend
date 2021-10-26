from django.contrib import admin
from .models import ExampleModel
from .models import Poll

# Register your models here.

admin.site.register(ExampleModel)
admin.site.register(Poll)