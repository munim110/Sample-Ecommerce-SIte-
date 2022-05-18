from django.urls import path
from . import views

urlpatterns = [
    path('viewcart/<int:user_id>', views.view_cart,name='viewcard')
]