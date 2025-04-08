from django.urls import path, include
from . import views




urlpatterns = [
    path('accounts/', include('account.urls')),
    path('', views.home, name="home"),  # Home page
    path('delete-task/<int:task_id>/', views.delete_task, name='delete_task'),
    # path('login/', login_view, name="login"), 


]

    # path('main/' , views.main , name='main'),
    # path('tasks/', task_list, name='task_list'),
    
    