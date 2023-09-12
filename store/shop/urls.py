from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r'list', IndexApi)
urlpatterns = [
    path('', index, name='home'),
    path('category/<int:pk>', CategoryView.as_view(), name='category'),
    path('search/', Search.as_view(), name='search'),
    path('detail/<int:pk>', product_item_detail, name='product_item_detail'),

    path('api/v1/', include(router.urls))
]
