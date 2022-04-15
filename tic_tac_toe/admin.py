import imp
from telnetlib import GA
from django.contrib import admin
from .models import Game


admin.site.register(Game)

