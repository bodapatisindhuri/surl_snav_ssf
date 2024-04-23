from django.urls import path
from app1.views import *

app_name='kind'

urlpatterns=[
    path('kind/',kind,name='kind'),
    path('peace/',peace,name='peace')
]