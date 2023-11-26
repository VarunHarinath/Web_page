from django.urls import path
from . import views

urlpatterns = [
    path('thankyou',views.thankyouPage,name="endpage")
]
