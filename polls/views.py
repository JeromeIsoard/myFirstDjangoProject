from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render

from pprint import pprint

User = get_user_model()


def index(request):
    print(request)
    users = User.objects.all()
    pprint(dir(User))
    context = {
        "users": users
    }

    return render(request, 'base.html', context=context)
