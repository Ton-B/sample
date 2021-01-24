from django.contrib import admin
from django.urls import path, include
from .views import samplefunc

urlpatterns = [
    path('sample/', samplefunc),
]
