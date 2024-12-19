from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('user/add/submition', views.user_add_submition, name="user-submition"),
    path('user/edit/<int:id>/', views.user_edit, name="user-edit"),
    path('user/edit/submition/<int:id>/', views.user_edit_submition, name="user-edit-submition"),
    path('user/delete/<int:id>/', views.user_delete, name="user-delete"),
    path('user/input', views.user_input, name="user-input"),
]