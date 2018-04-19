from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('<slug:slug>/', views.travellog),
    path('admin/', admin.site.urls),
    path('nested_admin/', include('nested_admin.urls')),
]
