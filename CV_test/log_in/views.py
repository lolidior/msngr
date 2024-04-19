from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import auth
from .forms import authForm

@login_required
def profile(request):
    form = authForm()

    data = {
        'form': form
    }

    return render(request, 'log_in/profile.html', data)
