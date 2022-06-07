from django.urls import path
from .views import AccountinformationView, CreateAccountView

app_name = 'users'
urlpatterns = [path('create-account/', CreateAccountView.as_view(),name='createAccount'),
    path('account-information/', AccountinformationView.as_view(),name='Account-Information')]