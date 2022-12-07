"""lalafo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf. urls.static import static
from apps.settings.views import index
from apps.products.views import product_detail, product_create, product_search
from apps.users.views import register, user_login
from django.contrib.auth.views import LogoutView
# from apps.products.views import products

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = "index"),
    path('product/<int:id>/',product_detail, name = "product_detail"),
    path('register/', register, name = "register"),
    path('logout/', LogoutView.as_view(next_page = "index"), name = "logout"),
    path('login/', user_login, name = "user_login"),
    path('product/create/', product_create, name = "product_create"),
    path('product/search/',product_search, name='product_search')

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
