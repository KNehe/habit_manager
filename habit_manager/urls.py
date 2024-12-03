"""
URL configuration for habit_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("tracker.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
]

# The Django ORM
# Database abstraction - API - SYSTEM
# CRUD - Create, Read, Update, Delete
# ORM - Object Relational Mapper

# SQL Queries
# 1. One language - python
# 2. tests python
# 3. data in python objects
# 4. automate validation in your objects(python)
# 5. Migrations, security, etc
