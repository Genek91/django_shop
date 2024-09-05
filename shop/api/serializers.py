from rest_framework import serializers
from django.contrib.auth.models import User
from versatileimagefield.serializers import VersatileImageFieldSerializer

from products.models import Product, Category, Subcategory
from cart.models import Cart, CartItem


class RegisterUserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user


class SubcategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Subcategory
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    subcategories = SubcategorySerializer(
        many=True, read_only=True, source='subcategory_set'
    )

    class Meta:
        model = Category
        fields = ('name', 'slug', 'image', 'subcategories')


class ProductSerializer(serializers.ModelSerializer):

    category = serializers.CharField(source='subcategory.category.name')
    subcategory = serializers.CharField(source='subcategory.name')
    image = VersatileImageFieldSerializer(
        sizes=[
            ('small', 'crop__100x100'),
            ('medium', 'crop__300x300'),
            ('large', 'crop__600x600'),
        ]
    )

    class Meta:
        model = Product
        fields = (
            'name', 'slug', 'category', 'subcategory', 'price', 'image'
        )


class CartItemSerializer(serializers.ModelSerializer):

    product = ProductSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ('product', 'quantity')


class CartSerializer(serializers.ModelSerializer):

    products = CartItemSerializer(
        many=True, read_only=True, source='cartitem_set'
    )
    total_items = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ('user', 'products', 'total_items', 'total_price')

    def get_total_items(self, obj):
        return sum(item.quantity for item in obj.cartitem_set.all())

    def get_total_price(self, obj):
        return sum(
            item.quantity * item.product.price
            for item in obj.cartitem_set.all()
        )
