from django.urls import path
from . import views

app_name = 'blogstory'

urlpatterns =[
    path('like', views.like, name='like'),
]

