from django.urls import path
from django.contrib import admin
from cores import views


urlpatterns = [
path('', views.HomeListView.as_view(), name='projects'),
path('detail2/<int:pk>',views.HomeDetailView.as_view(), name='detail_page2'),

]
