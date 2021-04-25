from django.urls import path

from . import views

urlpatterns = [
    path('', views.pass_gen, name='js'),
]