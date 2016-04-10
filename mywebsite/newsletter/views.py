from django.conf import settings
from django.shortcuts import render
from .forms import SignUpForm, ContactForm
from django.core.mail import send_mail
from .models import SignUp
# Create your views here.

def home(request):
    title = "Sign Up Now"
    form = SignUpForm(request.POST or None)
    # if request.user.is_authenticated():
    #     title = "Welcome %s" %(request.user)

    #add a form
    # if request.method == "POST":
    #     print request.POST
    context = {
        "title": title,
        "form":form,
    }

    if form.is_valid():
        instance = form.save(commit = False)
        instance.save()
        first_name = form.clean_first_name.get("first_name")
        if not first_name:
            first_name = "New full name"
        instance.first_name = first_name
        # print instance.last_name
        # print instance.email
        # print instance.timestamp
        context = {
        "title": "Thank You",
    }
    if request.user.is_authenticated() and request.user.is_staff:
        # print SignUp.objects.all()
        # for item in SignUp.objects.all:
        #     print item

        context = {
        "queryset": [123, 456],
    }

    return render(request, "home.html", context)

def contact(request):
    title = 'Contact Us.'
    form = ContactForm(request.POST or None)
    if form.is_valid():
        # for key, value in form.cleaned_data.iteritems():
        #     print key, value
        form_email = form.cleaned_data.get("email")
        form_message= form.cleaned_data.get("message")
        form_first_name = form.cleaned_data.get("first_name")
        form_last_name = form.cleaned_data.get("last_name")
        # print first_name, last_name, email, message

        subject ="site Contact Form"
        from_email = settings.EMAIL_HOST_USER
        to_email = ["cmmwaura@ucdavis.edu"]
        contact_message = "%s: %s via %s" %(
            form_first_name,
            form_last_name,
            form_message,
            form_email)
        send_mail(subject,
                  contact_message,
                  from_email,
                  to_email,
                  fail_silently=True)
    context ={
        "form": form,
        "title":title

    }
    return render(request, "forms.html", context)