from django.shortcuts import render
from .forms import msg_send
from .models import msgs
from main.models import User
from django.views.generic import DetailView


def Chat(request):
    print(User.username)
    error=''
    if request.method == "POST":
        form = msg_send(request.POST)
        if form.is_valid():
            candidate = form.save(commit=False)  # это нужно чтобы объект в модели создался, но зависимости пока не проверялись
            candidate.send = request.user.get_username()
            candidate.save()
            form.save()
        else:
            error='GRUSTNO'
    form = msg_send()
    viewmsgs = msgs.objects.all().order_by('-send_date')
    users = User.objects.all()
    im = request.GET.get("im")
    data = {
        'form': form,
        'error': error,
        'msgs': viewmsgs,
        'users': users,
        "im": im
    }
    return render(request, 'msgs/chat.html', data)




