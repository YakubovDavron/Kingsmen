from rest_framework import generics
from .models import *
from .seri import *


class SalesApiView(generics.ListAPIView):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer


class ColorApiView(generics.ListAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class SizeApiView(generics.ListAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer


class DistrictApiView(generics.ListCreateAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer


class ProductColorApiView(generics.ListAPIView):
    queryset = ProductColor.objects.all()
    serializer_class = ProductColorSerializer


class ProductSizeApiView(generics.ListAPIView):
    queryset = ProductSize.objects.all()
    serializer_class = ProductSizeSerializer


class OrderApiView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemApiView(generics.ListAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class VerifyPhoneApiView(generics.ListAPIView):
    queryset = VerifyPhone.objects.all()
    serializer_class = VerifyPhoneSerializer


class ProductApiView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class AccountApiView(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class CashbackHistoryApiView(generics.ListAPIView):
    queryset = CashbackHistory.objects.all()
    serializer_class = CashbackHistorySerializer


class ProductImageApiView(generics.ListAPIView):
    queryset = ProductImages.objects.all()
    serializer_class = ProductImageSerializer


class ProductVideoApiView(generics.ListAPIView):
    queryset = ProductVideo.objects.all()
    serializer_class = ProductVideoSerializer
