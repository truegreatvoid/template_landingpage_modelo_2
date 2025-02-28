from icecream import ic

from django.views.generic import TemplateView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.colaborador.models import *
from apps.landingpage.models import *
from apps.tabela.models import *


class Dashboard(TemplateView):
    model = LandingPage
    template_name = 'landingpage/home/dashboard.html'   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['eas'] = LandingPage.objects.first()
        context['programas'] = Programas.objects.all()
        context['oferecemos'] = Oferecemos.objects.all()
        context['eventos'] = Eventos.objects.all()
        context['colaboradores'] = Colaboradores.objects.all()
        return context
