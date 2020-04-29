from django.urls import path
from . import views


urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('task-list/', views.taskList, name="task-list"),
    path('task-detail/<str:pk>', views.taskDetail, name="task-details"),
    path("task-create/", views.createTask, name="create-task"),
    path("task-update/<str:pk>/", views.updateTask, name="update-task"),
    path("task-delete/<str:pk>/", views.deleteTask, name="delete-task")
]
