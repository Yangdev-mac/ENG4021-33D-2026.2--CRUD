from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('editar/<int:pk>/', views.editar, name='editar'),
    path('excluir/<int:pk>/', views.excluir, name='excluir'),
]
