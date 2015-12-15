from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView

from .models import Sponsor, Judge
from .forms import TeamForm


class TeamSignUp(SuccessMessageMixin, CreateView):
    form_class = TeamForm
    template_name = "index.html"
    success_message = "Team %(team_name)s was created successfully!"

    def get_context_data(self, **kwargs):
        context = super(TeamSignUp, self).get_context_data(**kwargs)

        context['organizers'] = Sponsor.objects.filter(category='Organizer')
        context['platinum_sponsors'] = Sponsor.objects.filter(category='Platinum')
        context['gold_sponsors'] = Sponsor.objects.filter(category='Gold')
        context['silver_sponsors'] = Sponsor.objects.filter(category='Silver')
        context['bronze_sponsors'] = Sponsor.objects.filter(category='Bronze')
        context['media_partners'] = Sponsor.objects.filter(category='Media')
        context['community_partners'] = Sponsor.objects.filter(category='Community')
        context['judges'] = Judge.objects.all()

        return context
