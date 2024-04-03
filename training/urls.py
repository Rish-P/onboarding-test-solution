from django.urls import path
from training import views 

urlpatterns = [
    path('', views.index, name="index"),
]