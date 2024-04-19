from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView

from log_in.forms import RegisterForm
#from .forms import msgtxt


def index(request):
    print('main page')
    data = {
        'title': 'Главная страница',
        'values': ['Some', 'Hello', '123'],
        'obj': {
            'car': 'LADA',
            'age': 18,
            'hobby': 'Programming'
        }
    }
    return render(request, 'main/index.html', data)
def about(request):
    print('about page')
    return render(request, 'main/about.html')

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy("log_in")
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



