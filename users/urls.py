from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = "users"

urlpatterns = [
    path('users/', views.user_list, name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
]