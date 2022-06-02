# endregion

# __init__.py
import sys
import os
import time
import datetime
import json
import logging
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'Cart'

urlpatterns = [
    # path('', (views.Index), name='Index'),
    path('', (views.Index), name='Index'),
]
# End of TFile
