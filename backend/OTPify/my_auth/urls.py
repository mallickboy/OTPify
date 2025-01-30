from django.urls import path

from . import views

# localhost:port/auth/
urlpatterns = [
    path('', views.auth_page, name="my_auth"),
    path('order/', views.order, name="my_auth/order"),
]