from django.urls import path

from . import views

urlpatterns = [
    path('product/', views.view_product, name='product'),
    
]