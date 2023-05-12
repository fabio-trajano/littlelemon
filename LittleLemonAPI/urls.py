from django.urls import path
from . import views

urlpatterns = [
    path('menu-items/', views.MenuItems.as_view()),
    path('menu-items/<int:pk>', views.Item.as_view()),
]
