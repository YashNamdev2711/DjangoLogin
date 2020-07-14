
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.demo,name='home'),
    path('cprog/', views.cprog,name='cprog'),
    path('javaprog/', views.javaprog,name='javaprog'),
    path('pythonprog/', views.pythonprog,name='pythonprog'),
    path('contact/', views.contact,name='contact'),
]
