from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detailed-view/<int:pk>/', views.Detailview.as_view(), name='detail'),
]
