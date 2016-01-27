from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# Register your models here.

from .forms import TeamForm
from .models import Team, Judge, Sponsor, TeamResource, SponsorResource
# Register your models here.


class TeamAdmin(ImportExportModelAdmin):
    resource_class = TeamResource
    list_display = ["__unicode__", "timestamp"]
    form = TeamForm

class JudgeAdmin(admin.ModelAdmin):
    pass

class SponsorAdmin(ImportExportModelAdmin):
    resource_class = SponsorResource
    pass



admin.site.register(Team, TeamAdmin)
admin.site.register(Judge, JudgeAdmin)
admin.site.register(Sponsor, SponsorAdmin)
