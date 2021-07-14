from django.urls import path 
from .views import login
from .views import inicio

urlpatterns = [
    path ('login.html',login,name="login"),
    path ('inicio.html',inicio,name='inicio'),
    path ('form.html',inicio,name='form')
]