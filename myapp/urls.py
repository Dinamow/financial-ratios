from django.urls import path
from .views import *

urlpatterns = [
    path('', testing, name='testing'),
    path('dates/', dates, name='dates'),
    path('balance/', balance, name='balance'),
    path('save/', save, name='save')
]