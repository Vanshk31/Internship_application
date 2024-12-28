from django.urls import path
from . import views  # Import the views module
from .views import login_view  # Import your view
from .api_views import register_api, login_api


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', login_view, name='login'),
    path('api/register/', register_api, name='register_api'),
    path('api/login/', login_api, name='login_api'),
]
