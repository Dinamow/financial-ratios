from django.urls import path
from .views import *

urlpatterns = [
    path('test/', testing, name='testing'),
    path('', landing, name='landing'),
    path('landing', landing, name='landing'),
    path('view_ratios', view_ratios, name='view_ratios'),
    path('compare_ratios', compare_ratios, name='compare_ratios'),
    path('add_company', add_company, name='add_company'),
    path('dates', dates, name='dates'),
    path('balance', balance, name='balance'),
    path('create', create, name='create'),
    path('save', save, name='save')
]