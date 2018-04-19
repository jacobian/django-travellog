from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>/', views.travellog),
    path('admin/', admin.site.urls),
]
