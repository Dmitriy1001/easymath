from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('equations/', views.equations_list, name='equations_list'),
    path('equations/<slug:equation_slug>/', views.equation_detail, name='equation_detail'),
]