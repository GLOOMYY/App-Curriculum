from django.urls import path, include
from .views import StackListView, ProjectDevListView, StackCreateView, StackUpdateView, ProjectDevCreateView, StackDeleteView

urlpatterns = [
    # Rutas de usuario
    path('stack/list', StackListView.as_view()),
    path('stack/create', StackCreateView.as_view()),
    path('stack/edit/<int:pk>', StackUpdateView.as_view()),
    path('stack/delete/<int:pk>', StackDeleteView.as_view()),
    
    path('projects/list', ProjectDevListView.as_view()),
    path('projects/create', ProjectDevCreateView.as_view()),

]
