from django.urls import path
from todo_app import views

urlpatterns = [
    path("",views.todo_list, name="list"),
    path("remove/<int:pk>/",views.todo_delete, name= "delete"),
    path("add/", views.todo_create, name="create"),
    path("edit/<int:pk>/", views.todo_update, name="update"),
]