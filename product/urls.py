from django.urls import path
from . import views

urlpatterns = [
    
    path('bank/', views.BankAPIView.as_view())
]