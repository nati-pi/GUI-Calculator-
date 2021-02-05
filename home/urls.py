from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('gp', views.another, name='gp'),
    path('gpa', views.calc, name='gpa'),
    path('cgpa', views.cgpa, name='cgpa')

]
