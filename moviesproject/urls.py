from django.contrib import admin
from django.urls import path
from moviesapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('editar/<int:pk>/', views.editar, name='editar'),
    path('excluir/<int:pk>/', views.excluir, name='excluir'),
]
