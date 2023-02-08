from django.urls import path
from apps.example import views

app_name = "example"

urlpatterns = [
    path("<int:amount>", views.UsersView.as_view(), name="users"),
    path("", views.UsersView.as_view(), name="users"),
]
