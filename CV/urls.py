from django.urls import path
from . import views

urlpatterns = [
    path('', views.rishik_cv, name="CV"),
]