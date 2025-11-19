from django.urls import path
from . import views

urlpatterns = [
    path('', views.dog_image_view, name='dog_image'),  # главная страница
]