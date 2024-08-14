from django.contrib import admin

# Register your models here.

from django.apps import apps
from .models import CustomUser
# Register your models here.
admin.site.register(CustomUser)



app = apps.get_app_config('graphql_auth')

for model_name, model in app.models.items():
    admin.site.register(model)