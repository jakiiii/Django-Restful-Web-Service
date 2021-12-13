from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from accounts.views import registration_view, logout_view

app_name = "account"


urlpatterns = [
    # path('api-auth/', include('rest_framework.urls')),
    path('login/', obtain_auth_token, name='login-api'),
    path('registration/', registration_view, name='registration-api'),
    path('logout/', logout_view, name='logout-api'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
