from django.urls import path, include
from .views import RegisterView


urlpatterns = [
    path('auth/login', RegisterView.as_view(), name='googleUser'),
]
