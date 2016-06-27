from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password

from presbid.accounts.models import CustomUser

class CustomRegistration(UserCreationForm):
    email = forms.EmailField(required=True,
            widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter your email'}))
    first_name = forms.CharField(
            widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter your first name'}))
    last_name = forms.CharField(
            widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter your last name'}))

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number','first_name', 'last_name', 'password1', 'password2')

    def save(self,commit=True):
        CustomUser = super(UserCreationForm, self).save(commit = False)
        CustomUser.email = self.cleaned_data['email']
        CustomUser.phone_number = self.cleaned_data['phone_number']
        CustomUser.first_name = self.cleaned_data['first_name']
        CustomUser.last_name = self.cleaned_data['last_name']
        CustomUser.password = make_password(password = self.clean_password2(), salt=None, hasher='pbkdf2_sha256')

        if commit:
            CustomUser.save()

        return CustomUser

    def __init__(self, *args, **kwargs):
        super(UserCreationForm,self).__init__(*args,**kwargs)
        for first_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'