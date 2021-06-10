from django.urls import path
from .views import *
app_name = 'Home'

urlpatterns = [
   path('index/',Index,name='Home'),
   path('common/',Common),
   
]
