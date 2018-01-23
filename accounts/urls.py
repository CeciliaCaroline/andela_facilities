from django.urls import path, include
from .views import home


urlpatterns = [
    path('oauth/', include('social_django.urls', namespace='social')),
    path('home', home, name='home'),
]
