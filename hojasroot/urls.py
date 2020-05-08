from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('community/', views.community, name='community'),
    path('about/', views.about, name='about')
]
