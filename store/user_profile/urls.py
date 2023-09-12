from django.urls import path, include
from .views import *

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),

    path('logout/', logout_user, name='logout'),
    path('profile/', ProfilePage.as_view(), name='profile'),
    path('api/v1/register/', RegisterAPIView.as_view()),
    path('api/v1/auth/', include('rest_framework.urls')),
    path('api/v1/profile', ProfilePageApiView.as_view())
]
