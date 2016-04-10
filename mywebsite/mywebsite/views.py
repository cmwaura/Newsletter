__author__ = 'crispus'

from django.shortcuts import render
from django.conf import settings
# from .forms import SignUpUsers, Userform
from django.core.mail import send_mail


# Create your views here.

def about(request):

    return render(request, "about.html", {})




def profile(request):

    # if request.user.is_authenticated() and request.user.is_staff:
    #     context = {
    #     "queryset": [123, 456],
    # }

    return render(request, "profile.html", {})
