from django.urls import path, include
from .views import (OrderCreateView, UserProOrderListView, 
                UserProOrderUpdateView,UserProOrderDeleteView, favorite_orders)
app_name = "orders"
urlpatterns = [
    path('userpro-create-order/', OrderCreateView.as_view(), name="userpro-create-order" ),
    path('userpro-orders/<str:username>/', UserProOrderListView.as_view(), name="userpro-orders" ),
    path('userpro-orders/<int:pk>/update/', UserProOrderUpdateView.as_view(), name="userpro-order-update" ),
    path('userpro-order/<int:pk>/delete/', UserProOrderDeleteView.as_view(), name='userpro-order-delete' ),

    path('<int:pk>/favorite_order/', favorite_orders, name='favorite_orders')
]
