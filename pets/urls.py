"""
URL configuration for pets project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from app import views
from pets import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, ),
    path('buyer_register', views.buyer_register, name='buyer_register'),
    path('login_view', views.login_view, name='login_view'),
    path('buyer_panel', views.buyer_panel, name='buyer_panel'),
    path('pet_register', views.pet_register, name='pet_register'),
    path('buyer_pet_view', views.buyer_pet_view, name='buyer_pet_view'),
    path('pet_view', views.pet_view, name='pet_view'),
    path('pet_update/<int:id>/', views.pet_update, name='pet_update'),
    path('pet_delete/<int:id>/', views.pet_delete, name='pet_delete'),
    path('seller_panel', views.seller_panel, name='seller_panel'),
    path('Logout', views.Logout, name='Logout'),
    path('buyer_profile/<int:id>/', views.buyer_profile, name='buyer_profile'),
    path('buyer_update/<int:id>/', views.buyer_update, name='buyer_update')



]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
