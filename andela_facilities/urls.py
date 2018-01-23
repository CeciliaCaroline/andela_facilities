from django.urls import include, path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from rest_framework_jwt.views import (refresh_jwt_token, verify_jwt_token,
                                      obtain_jwt_token)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.login),
    path('accounts/', include('accounts.urls')),
    path('refresh-token/', refresh_jwt_token, name='refresh token'),
    path('verify-token/', verify_jwt_token, name='verify token'),
    path('obtain-token/', obtain_jwt_token, name='obtain token'),
    path('spaces/', include('space.urls')),

]
