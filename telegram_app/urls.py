from django.urls import path
from . import views  # assuming your view is in the same app's views.py file

urlpatterns = [
    path('generate', views.process_request, name='generate'),
]
