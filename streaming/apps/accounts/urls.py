from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from apps.accounts.views import registration_view, logout


urlpatterns = [
    # path('login/', obtain_auth_token, name='login'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('registration/', registration_view, name='registration'),
    path('logout/', logout, name='logout'),
]
