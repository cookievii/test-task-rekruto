from api import views
from django.urls import path

app_name = "api"

urlpatterns = [
    path("", views.main, name="main"),
]
