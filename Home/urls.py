import sys
import os
import time
import datetime
import json
import logging
from django.urls import path
from . import views

app_name = 'Home'

urlpatterns = [
     # path('contact/', (views.ContactView), name='ContactView'),
     path('', (views.IndexView), name='IndexView'),
     path('login/', (views.LoginView), name='login'),
     path('registers/', (views.RegistersView), name='registers'),
     path('logout/', (views.logout_view), name='logout_view'),
]