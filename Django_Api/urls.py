from django.contrib import admin
from django.urls import path, include

from Shoes import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'manufacturers', views.ManufacturerViewSet)
router.register(r'shoetypes', views.ShoeTypeViewSet)
router.register(r'shoecolors', views.ShoeColorViewSet)
router.register(r'shoes', views.ShoeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
