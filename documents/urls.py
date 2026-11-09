from django.urls import path
from . import views

urlpatterns = [
    path("", views.upload_document, name="upload"),
    path("summarize/<int:pk>/", views.summarize_document, name="summarize"),
]