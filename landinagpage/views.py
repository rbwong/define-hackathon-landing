from django.shortcuts import render
from .forms import TeamForm
from .models import Team
from django.views.generic.edit import CreateView
# Create your views here.

class TeamSignUp(CreateView):
	form_class = TeamForm
	template_name = "index.html"