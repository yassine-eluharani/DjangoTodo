from django.urls import path
from . import views
from .views import TodoDetailApiView

urlpatterns = [
    path("create", views.post),
    path("all", views.get),
    path("todo/<int:todo_id>", TodoDetailApiView.as_view())
]
