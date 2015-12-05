from .forms import TeamForm
from django.views.generic.edit import CreateView
from .models import Sponsor, Judge

# Create your views here.


class TeamSignUp(CreateView):
    form_class = TeamForm
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(TeamSignUp, self).get_context_data(**kwargs)

        context['co_presentors'] = Sponsor.objects.all()
        context['judges'] = Judge.objects.all()

        return context
