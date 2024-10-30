from django.urls import path
from . import views

urlpatterns = [
    #declaring all the URLs right here
    path('', views.home, name='home-page'),
    path('add/', views.add_task, name='add-task'),
    path('complete/<int:id>/', views.complete_task, name='complete-task'),
    path('update_status/<int:task_id>/', views.update_status, name='update-status'),
    path('delete-task/<int:task_id>/', views.delete_task, name='delete-task'),
]