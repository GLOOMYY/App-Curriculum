from django.urls import path
from .views import *

urlpatterns = [
    path('', PerfilView.as_view(), name='curriculum'),
]
