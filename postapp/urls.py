from django.urls import path, include
from . import views
urlpatterns = [

    path('viewpost/', views.viewall, name="viewall"),
    path('addpost/', views.add, name="add"),

]
