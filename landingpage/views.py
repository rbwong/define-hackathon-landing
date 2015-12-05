from .forms import TeamForm
from django.views.generic.edit import CreateView
# Create your views here.


class TeamSignUp(CreateView):
    form_class = TeamForm
    template_name = "index.html"
