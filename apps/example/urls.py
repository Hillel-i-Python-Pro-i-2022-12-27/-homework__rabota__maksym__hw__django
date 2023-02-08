from django.urls import path
from apps.example import views

app_name = "example"

urlpatterns = [
    path("<int:amount>", views.UsersView.as_view(), name="users_wiht_amount"),
    path("", views.UsersView.as_view(), name="users_with_amount"),
]
