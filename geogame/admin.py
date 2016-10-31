from django.contrib import admin
from geogame.models import Scenario


class ScenarioAdmin(admin.ModelAdmin):
    pass

admin.site.register(Scenario, ScenarioAdmin)
