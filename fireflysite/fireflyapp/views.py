from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    return render(request, "index.html")


def userhome(request):
    return render(request, "userhome.html")


def is_member_basic(request):
    return request.groups.filter(name='Basic').exists()


def user_account_settings(request):
    return render(request, "account_settings.html")

