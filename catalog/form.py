from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import User


class Logform(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        user = self.cleaned_data.get("username")
        passw = self.cleaned_data.get("password")
        val = authenticate(username=user, password=passw)
        if val == None:
            raise forms.ValidationError("Invalid Credentials")


class Userform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    retype_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

