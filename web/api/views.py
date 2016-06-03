from api.serializers import *
from api.models.product import Product
from api.models.banners import Slider
from api.models.category import Category
from api.models.filters import ProductFilter
from rest_framework import viewsets, filters, views, response, status
from api.models.pagination import ProductListPagination
from api.models.order import Order
from api.models.user import User
from django.core.mail import send_mail
from smtplib import SMTPException


# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().filter(enabled=True)
    serializer_class = ProductSerializer
    pagination_class = ProductListPagination
    http_method_names = ['get']
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filter_class = ProductFilter
    ordering_fields = ('time_add', 'price', 'is_preorder', 'title')
    lookup_field = 'url'
    search_fields = ('title',)


class SliderViewSet(viewsets.ModelViewSet):
    queryset = Slider.objects.all().filter(enabled=True)
    serializer_class = SliderSerializer
    http_method_names = ['get']


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().filter(enabled=True)
    serializer_class = CategorySerializer
    http_method_names = ['get']
    lookup_field = 'url'


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EmailView(views.APIView):
    def post(self, request, *args, **kwargs):
        user_email = request.data.get('email')
        email_theme = request.data.get('theme')
        from_who = request.data.get('from')
        body = request.data.get('body')

        try:
            send_mail(email_theme, '', from_who, [user_email], html_message=body, fail_silently=False)
        except SMTPException:
            return response.Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return response.Response({'success': True}, status=status.HTTP_201_CREATED)
