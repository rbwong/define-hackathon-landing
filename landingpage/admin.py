from django.contrib import admin

# Register your models here.

from .forms import TeamForm
from .models import Team, Judge, Sponsor
# Register your models here.


class TeamAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "timestamp"]
    form = TeamForm

class JudgeAdmin(admin.ModelAdmin):
	pass

class SponsorAdmin(admin.ModelAdmin):
	pass



admin.site.register(Team, TeamAdmin)
admin.site.register(Judge, JudgeAdmin)
admin.site.register(Sponsor, SponsorAdmin)