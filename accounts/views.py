import os
from rest_framework import generics, permissions
from oauth2client import crypt, client
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework_jwt.settings import api_settings
from .models import User
from .serializers import UserSerializer
from django.contrib.auth.models import Group


def google_validation(request):
    token = request.data.get('token')
    CLIENT_ID = os.getenv('CLIENT_ID')
    token.replace(" ", "")

    try:
        # Specify the CLIENT_ID of the app that accesses the backend:
        idinfo = client.verify_id_token(
            token,
            CLIENT_ID)

        if 'hd' not in idinfo:
            return Response(
                'no hd key', status=status.HTTP_401_UNAUTHORIZED)

        if idinfo['iss'] not in ['accounts.google.com',
                                 'https://accounts.google.com']:
            return Response('Wrong issuer.', status.HTTP_401_UNAUTHORIZED)

        # If auth request is not from the andela domain:
        # or email is not verified or
        # no client id returned by google
        if idinfo['hd'] != 'andela.com' or \
            not idinfo['email_verified'] or \
                idinfo['aud'] != CLIENT_ID:
            body = 'Invalid parameters given'
            return Response(
                body, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        # if all checks pass, user information is returned
        if idinfo['hd'] == 'andela.com' and \
            idinfo['email_verified'] is True and \
                idinfo['aud'] == CLIENT_ID:
            return idinfo

    # Invalid token
    except crypt.AppIdentityError:
        body = 'Invalid Token'
        return Response(
            body,
            status=status.HTTP_401_UNAUTHORIZED)


def get_auth_token(user):
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
    payload = jwt_payload_handler(user)
    token = jwt_encode_handler(payload)

    serializer = UserSerializer(user)

    body = {
        'token': token,
        'user': serializer.data
    }
    return body


class RegisterView(generics.CreateAPIView):
    """View to register google users"""
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        """Custom method to handle post requets"""

        response = google_validation(request)
        if isinstance(response, dict):
            try:
                userid = response['sub']
                user = User.objects.get(google_id=userid)

            except User.DoesNotExist:
                user = User.objects.create(
                    username=response['name'],
                    google_id=response['sub'],
                    appuser_picture=response['picture'])
                user.save()

                # assign new user to group
                my_group = Group.objects.get(name='Fellows')
                my_group.user_set.add(user)

            body = get_auth_token(user)
            return Response(body, status=status.HTTP_201_CREATED)
        return response




# class GoogleUserView(generics.GenericAPIView):
#     """List Google User by Id."""
#     model = User
#     serializer_class = UserSerializer

#     def get(self, request):
#         """Custom method to handle get requets"""
#         # import pdb;pdb.set_trace()
#         user_id = self.request.user.id
#         try:
#             app_user = User.objects.get(id=user_id)
#         except User.DoesNotExist:
#             raise Http404

#         serializer = UserSerializer(app_user)
#         return Response(serializer.data)
