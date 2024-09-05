from django.shortcuts import get_object_or_404
from rest_framework import mixins, viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token

from products.models import Category, Product
from cart.models import Cart, CartItem
from api.serializers import (RegisterUserSerializer, ProductSerializer,
                             CategorySerializer, CartSerializer,
                             CartItemSerializer)


class UserViewSet(viewsets.ViewSet):

    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'user': serializer.data['username'],
            'token': token.key
        }, status=status.HTTP_201_CREATED)


class CategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):

    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer


class ProductViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):

    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer


class CartViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        cart, created = (
            Cart.objects
            .prefetch_related('cartitem_set__product')
            .get_or_create(user=request.user)
        )
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    @action(detail=False, methods=['post', 'put', 'delete'])
    def items(self, request):
        product_id = request.data.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        cart, created = Cart.objects.get_or_create(user=request.user)

        if request.method == 'POST':
            cart_item, created = CartItem.objects.get_or_create(
                cart=cart, product=product
            )
            cart_item.quantity = (
                (cart_item.quantity or 0) + request.data.get('quantity', 1)
            )
            cart_item.save()
            serializer = CartItemSerializer(cart_item)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'PUT':
            cart_item = get_object_or_404(CartItem, cart=cart, product=product)
            cart_item.quantity = request.data.get('quantity')
            cart_item.save()
            serializer = CartItemSerializer(cart_item)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'DELETE':
            cart_item = get_object_or_404(CartItem, cart=cart, product=product)
            cart_item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['delete'])
    def clear(self, request):
        cart = get_object_or_404(Cart, user=request.user)
        cart.cartitem_set.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
