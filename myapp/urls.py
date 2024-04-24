from django.urls import path
from .views import *

urlpatterns = [
    path('test/', testing, name='testing'),
    path('', landing, name='landing'),
    path('one', one_year, name='one_year'),
    path('Compare', compare, name='compare'),
    path('dates', dates, name='dates'),
    path('balance', balance, name='balance'),
    path('create', create, name='create'),
    path('save', save, name='save')
]