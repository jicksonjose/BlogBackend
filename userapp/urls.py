from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.viewall, name="viewall"),
    path('add/', views.add, name="add"),
  

]
