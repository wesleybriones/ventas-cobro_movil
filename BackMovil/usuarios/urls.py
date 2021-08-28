from django.urls import path
from . import views

urlpatterns = [
    path('vendedor/', views.vendedor, name='vendedor'),
    path('login/', views.index, name='login')
]