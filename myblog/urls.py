from django.urls import path
from django.views.static import serve
from django.conf import settings
from . import views

app_name = 'myblog'


urlpatterns=[
    path('', views.index, name='index'),

    path('tag/<slug:tag_slug>', views.all_stories, name='tutorial_by_tag'),
    path('category/<slug:category_slug>', views.all_stories, name='categories_by_category'),
    path('all_stories', views.all_stories, name='all_stories'),
    path('details/<str:id>/<str:slug>', views.details, name='details'),
    path('search', views.searched, name='search'),
]