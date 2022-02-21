"""ShoppingCenter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from contact.views import ContactView, AboutUs

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include("products.urls")),
    path('conatct_us/', ContactView.as_view(), name="contact"),
    path('about_us/', AboutUs.as_view(), name="about"),
    path('costumers/', include('customers.urls')),
    path('login/', LoginView.as_view(), name="login"),
    # api and rosseta
    # path('api/v1/product/', include('products.urls')),
    path('api/v1/order/', include('orders.urls')),
    path('rosseta/', include('rosetta.urls')),
    # account
    path('accounts/', include('django.contrib.auth.urls')),
    path('api-auth/', include('rest_framework.urls')),
    prefix_default_language=True,
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
