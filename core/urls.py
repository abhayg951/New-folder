from django.urls import path
from .views import *

urlpatterns = [
    path("pdf", GeneratePdfView.as_view())
]
