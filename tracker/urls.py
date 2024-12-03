from django.urls import path
from .views import habit_list, logout_view, add_habit,\
    delete_habit, habit_detail, edit_habit, \
        add_log, change_habit_log_status, register
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", view=habit_list, name="habit_list"),
    path("accounts/login/", \
         view=auth_views.LoginView.as_view(template_name='tracker/login.html'), \
            name='login'),
    path('logout/', view=logout_view, name="logout"),
    path('add/', view=add_habit, name='add_habit'),
    path("delete/<int:pk>", view=delete_habit, name="delete_habit"),
    path("habit/<int:pk>", view=habit_detail, name="habit_detail"),
    path("habit/<int:pk>/edit/", view=edit_habit, name='edit_habit'),
    path("habit/<int:pk>/log/", view=add_log, name='add_log'),
    path("status/<int:pk>/", view=change_habit_log_status, name='status'),
    path("acounts/register/", view=register, name="register")
]