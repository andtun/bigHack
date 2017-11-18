from django.conf.urls import url
from django.shortcuts import render
from django.shortcuts import redirect

urlpatterns = [
    url(r'^$', lambda r: redirect('test')),
    url(r'^test/$', lambda r: render(r, 'test.html'), name='test'),
]
