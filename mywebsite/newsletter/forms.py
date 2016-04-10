__author__ = 'crispus'

from django import forms
from .models import SignUp

class ContactForm(forms.Form):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField()


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['first_name', 'last_name', 'email']
        ##exclude =["full name"] use this sparingly as possible.


    def clean_email(self): #instances of the field email
        email = self.cleaned_data.get('email')
        email_base, provider = email.split("@")
        domain, extension = provider.split('.')

        # if domain !="ucdavis":
        #     raise forms.ValidationError("Please use a valid U.C. DAVIS address")

        if extension != "edu":
            raise forms.ValidationError("Please use a valid .EDU address")
        return email
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        #validation code
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        #validation code
        return last_name

