from django.urls import path  

from . import views


urlpatterns = [
    path('', views.UrlListAPIView.as_view(), name='list'),
    path('urls/<int:pk>/', views.UrlDetailAPIView.as_view(), name='detail'),
    
]
