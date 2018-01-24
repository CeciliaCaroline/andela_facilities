from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_jwt.views import (refresh_jwt_token, verify_jwt_token,
                                      obtain_jwt_token)
from .views import RegisterView, GoogleUserView


urlpatterns = [
    path('user/', GoogleUserView.as_view(), name='app_user'),
    path('auth/', include([
        path('login', RegisterView.as_view(), name='googleUser'),
        path('refresh-token/', refresh_jwt_token, name='refresh token'),
        path('verify-token/', verify_jwt_token, name='verify token'),
        path('obtain-token/', obtain_jwt_token, name='obtain token'),
    ]))
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])
