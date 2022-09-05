from django.urls import path, include

from .views import (
    add_to_cart,
    delete_from_cart,
    order_details,
    checkout,
    update_transaction_records,
    success,
    SaveScreenshot
)


urlpatterns = [
    path('add-to-cart/<int:pk>/', add_to_cart, name="add_to_cart"),
    path('order-summary/', order_details, name="order_summary"),
    path('success/', success, name='purchase_success'),
    path('item/delete/<int:pk>/', delete_from_cart, name='delete_item'),
    path('checkout/', checkout, name='checkout'),
    path('update-transaction/<int:pk>/', update_transaction_records, name='update_records'),
    path('api/save_screenshot', SaveScreenshot.as_view(), name='save-screenshot')
]