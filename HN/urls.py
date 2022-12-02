from django.urls import path
from . import views

# urls goes here

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('comment', views.post_list_comment, name='comment'),
    path('story', views.post_list_story, name='story'),
    path('job', views.post_list_job, name='job'),
    path('poll', views.post_list_poll, name='poll'),
    path('pollopt', views.post_list_pollopt, name='pollopt'),
    path('<int:id>/',
         views.post_detail,
         name='post_detail'),
    path('search/', views.post_search, name='post_search'),
    path('load', views.load_db, name='load_db')
]
