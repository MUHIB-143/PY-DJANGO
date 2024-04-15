from django.urls import path

from hello import views

urlpatterns = [
    path('home/', views.home),
    path('muhib/', views.muhib),
    path('auth/', views.auth),
]
