from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from accounts.views import registration_view, logout_view


app_name = "account"


urlpatterns = [
    path('login/', obtain_auth_token, name='login-api'),
    path('registration/', registration_view, name='registration-api'),
    path('logout/', logout_view, name='logout-api'),
]
