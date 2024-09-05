from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework import routers

from api.views import UserViewSet, ProductViewSet, CategoryViewSet, CartViewSet

app_name = 'api'

router = routers.SimpleRouter()

router.register(
    'users', UserViewSet, basename='user'
)
router.register(
    'categories', CategoryViewSet, basename='categories'
)
router.register(
    'products', ProductViewSet, basename='products'
)
router.register(
    'cart', CartViewSet, basename='cart'
)

urlpatterns = [
    path('users/token/', views.obtain_auth_token, name='user-token'),
    path('', include(router.urls)),
]
