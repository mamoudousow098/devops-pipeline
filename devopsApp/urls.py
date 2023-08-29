from django.urls import path
from devopsApp import views



urlpatterns = [
    path("", views.home_view),
    
]