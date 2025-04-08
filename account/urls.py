from django.urls import path, include
from . import views

from . import views

urlpatterns = [
    path('register/', views.registration_view, name="register"),  # Register view
    path('logout/', views.logout_view, name="logout"),  # Logout view
    path('login/', views.login_view, name="login"),  # Login view
]
