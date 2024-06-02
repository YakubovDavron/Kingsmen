from django.urls import path
from .views import *

urlpatterns = [
    path('sales/', SalesApiView.as_view(), name='sales'),
    path('color/', ColorApiView.as_view(), name='color'),
    path('size/', SizeApiView.as_view(), name='size'),
    path('district/', DistrictApiView.as_view(), name='district'),
    path('product_color/', ProductColorApiView.as_view(), name='product_color'),
    path('product_size/', ProductSizeApiView.as_view(), name='product_size'),
    path('order/', OrderApiView.as_view(), name='order'),
    path('order_item/', OrderItemApiView.as_view(), name='order_item'),
    path('verify_phone/', VerifyPhoneApiView.as_view(), name='verify_phone'),
    path('product/', ProductApiView.as_view(), name='product'),
    path('account/', AccountApiView.as_view(), name='account'),
    path('cashback_history/', CashbackHistoryApiView.as_view(), name='cashback_history'),
    path('product_image/', ProductImageApiView.as_view(), name='product_image'),
    path('product_video/', ProductVideoApiView.as_view(), name='product_video'),
]
