from django.urls import path
from .views import TopBackView
from .views import ZayavkaView

from . import views


urlpatterns = [
    path('topes/', views.TopBackView.as_view(), name='topback_view'),
    path('zayavka/', views.ZayavkaView.as_view(), name='zayavka_view')


]
