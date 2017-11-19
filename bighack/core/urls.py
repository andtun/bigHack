from django.conf.urls import url
from django.shortcuts import redirect
from .views import *

urlpatterns = [
    url(r'^$', lambda r: redirect('home')),
    url(r'^home/$', home, name='home'),
    url(r'^apply/$', apply, name='apply'),
    url(r'^buildings/$', buildings, name='buildings'),
]
