from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login') #it helps use to go to login url after creting account
    template_name = 'users/createAccount.html'

class AccountinformationView(generic.TemplateView):
    template_name='users/accountinfor.html'
