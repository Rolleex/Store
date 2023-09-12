from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=55, label='Логин',
                               widget=forms.TextInput(attrs={'class': 'form-control', }))
    password1 = forms.CharField(label='Пароль', max_length=25,
                                widget=forms.PasswordInput(attrs={'class': 'form-control', }))
    password2 = forms.CharField(label='Подтверждение пароля',
                                widget=forms.PasswordInput(attrs={'class': 'form-control', }))
    email = forms.EmailField(label='Емейл',
                             widget=forms.EmailInput(attrs={'class': 'form-control', }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=55,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}))
    password = forms.CharField(max_length=25,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'off'}))


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'address', 'city', 'photo',)
