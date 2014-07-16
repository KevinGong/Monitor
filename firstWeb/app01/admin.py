from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.models import User as djangouser,Group as djangogroup
from app01.models import *
admin.site.register(IP)

# Register your models here.
