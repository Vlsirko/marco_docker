"""marco URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from api import views
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'slider', views.SliderViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'order', views.OrderViewSet)
router.register(r'user', views.UserViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'api/email/', views.EmailView.as_view()),
    url(r'^api/', include(router.urls)),
    url(r'^api/',  include('rest_framework.urls', namespace='rest_framework')),
    url(r'^tinymce/', include('tinymce.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
