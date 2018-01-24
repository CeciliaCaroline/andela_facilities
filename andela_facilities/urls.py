from django.urls import include, path
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.login),
    path('accounts/', include('accounts.urls')),
    path('spaces/', include('space.urls')),

]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])
