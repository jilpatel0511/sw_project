from django.urls import path
from .views import *
urlpatterns = [
   path('index/',Index),
   path('common/',Common),
]
