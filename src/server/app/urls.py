from django.urls import path, include
from . import views


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.register, name='register'),
    path('', views.dashboard, name='dashboard'),
]
