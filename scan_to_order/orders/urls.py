from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('menu/<int:table_number>/', views.menu_view, name='menu'),
    path('order/<int:table_number>/', views.place_order, name='place_order'),
]
