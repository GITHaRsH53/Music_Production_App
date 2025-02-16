from django.contrib import admin
from home.models import Contact #we imported only one model from models.py as we have only one model

# Register your models here.
admin.site.register(Contact)  # register Contact model in admin panel
# for passwords