from django.urls import path
from . import views

urlpatterns = [
    # o nome servirá para fazer o 'reverse look-up' para as routes
    path('', views.home, name='blog-home'), 
    path('about/', views.about, name='blog-about'), 
]
