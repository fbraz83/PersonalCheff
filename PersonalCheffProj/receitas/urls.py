from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sucodelaranja', views.sucodelaranja, name='sucodelaranja'),
    path('sucodelimao', views.sucodelimao, name='sucodelimao'),
    path('caipirinhadelimao', views.caipirinhadelimao, name='caipirinhadelimao')
]
