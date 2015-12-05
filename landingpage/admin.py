from django.contrib import admin

# Register your models here.

from .forms import TeamForm
from .models import Team
# Register your models here.


class TeamAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "timestamp"]
    form = TeamForm


admin.site.register(Team, TeamAdmin)
