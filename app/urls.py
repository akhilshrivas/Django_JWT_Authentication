from django.urls import path

from .views import RegisterView, ProfileView, UserListView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('profile/', ProfileView.as_view()),
    path('users/', UserListView.as_view()),   # 👈 NEW
]
