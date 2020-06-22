from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('<int:id>/', views.book_page, name = 'book_info_page'),
    path('<int:book_id>/cart/',views.add_to_cart, name = 'cart'),
    path('cart/',views.cart,name = 'actual_cart'),
    path('bill/<int:book_id>/',views.bill,name = 'bill'),
    path('orders/',views.orders,name = 'orders'),
]