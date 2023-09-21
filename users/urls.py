from django.urls import path
from .views import update_count
urlpatterns = [
    path('delay/',update_count)
]
