from django.urls import path
from app.views import *

app_name='style'

urlpatterns=[
    path('style/',style,name='style'),
    path('forgive/',forgive,name='forgive'),
]

