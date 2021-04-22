from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create ),
    path('update/', views.update ),
    path('read/', views.read )
]