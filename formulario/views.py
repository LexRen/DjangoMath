from django.shortcuts import render
from django.http import HttpResponse
from formulario.forms import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from formulario.models import basede2



def listar(request):
    a = basede2.objects.all()
    context = {
        'modelo': a
    }
    return render(request, "numeros.html", context)

    
class RegistroUsuario(CreateView):
	model = User
	template_name = "registro.html"
	form_class = RegistroForm
	success_url = '/accounts/login'

class yave(LoginRequiredMixin, CreateView):
    model = basede2
    template_name = "modsegu.html"
    fields = ['edad']
    success_url = '/lal'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class lista(ListView):
    model = basede2
    template_name = 'lista.html'


