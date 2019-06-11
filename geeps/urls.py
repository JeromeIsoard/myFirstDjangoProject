from django.urls import path

from . import views

urlpatterns = [
    path('', views.poster_printing_request, name='poster_printing_request'),
    path('/printing_request/', views.poster_printing, name='printing'),
]
