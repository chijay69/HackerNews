from django.urls import path
from . import views

# urls here

urlpatterns = [
    path('', views.getData, name='getdata'),
    path('add/', views.postData, name='postdata'),
]
