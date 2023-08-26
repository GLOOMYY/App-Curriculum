from django.urls import path, include
from .views import StackListView, ProjectDevListView

urlpatterns = [
    # Rutas de usuario
    path('stack/list', StackListView.as_view()),
    # path('create', RetreiveUpdateUserView.as_view()),
    # path('edit', CreateTokenView.as_view()),
    # path('delete', CreateTokenView.as_view()),
    
    path('projects/list', ProjectDevListView.as_view()),

]
