from django.urls import path

from . import views

urlpatterns = [
    path('', views.poster_printing_request, name='poster_printing_request'),
    path('/poster_printing/', views.poster_printing, name='poster_printing'),
]
