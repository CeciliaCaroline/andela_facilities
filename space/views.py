from rest_framework import generics, mixins, permissions
from rest_framework.response import Response
from rest_framework import status
from django.http import QueryDict
from andela_facilities.permissions import IsFacilities
from .serializers import SpaceSerializer, RoomSerializer, OccupantsSerializer
from .models import Space, Room, Occupant


# Create your views here.

class CreateView(generics.CreateAPIView):
    """This class defines the create behavior of the space."""
    queryset = Space.objects.all()
    serializer_class = SpaceSerializer
    permission_classes = (
        permissions.IsAuthenticated, IsFacilities)

    def perform_create(self, serializer):
        """Save create serializer"""
        serializer.save(owner=self.request.user)


class ViewSpace(mixins.ListModelMixin, generics.GenericAPIView):
    """This class defines the view behavior of the space."""
    queryset = Space.objects.all()
    serializer_class = SpaceSerializer
    permission_classes = (
        permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        """Method to view the list of spaces"""
        return self.list(request, *args, **kwargs)


class UpdateSpace(mixins.UpdateModelMixin, generics.GenericAPIView):
    """This class defines the update  behavior of the space."""
    queryset = Space.objects.all()
    serializer_class = SpaceSerializer
    permission_classes = (
        permissions.IsAuthenticated, IsFacilities)

    def put(self, request, *args, **kwargs):
        """Method to update a space"""
        return self.update(request, *args, **kwargs)


class DeleteSpace(mixins.DestroyModelMixin, generics.GenericAPIView):
    """This class defines the delete behavior of the space."""
    queryset = Space.objects.all()
    serializer_class = SpaceSerializer
    permission_classes = (
        permissions.IsAuthenticated, IsFacilities)

    def delete(self, request, *args, **kwargs):
        """Method to delete a space"""
        return self.destroy(request, *args, **kwargs)


class RetrieveSpace(mixins.RetrieveModelMixin, generics.GenericAPIView):
    """This class defines the view behavior of the space."""
    queryset = Space.objects.all()
    serializer_class = SpaceSerializer
    permission_classes = (
        permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        """Method to retrieve a single space"""
        return self.retrieve(request, *args, **kwargs)

##############################################


class CreateRoom(generics.CreateAPIView):
    """This class defines the create behavior of the room."""
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    lookup_url_kwarg = "space"
    permission_classes = (
        permissions.IsAuthenticated, IsFacilities)

    def create(self, request, *args, **kwargs):
        """Custom method to create a room"""
        space = self.kwargs.get(self.lookup_url_kwarg)
        if isinstance(request.data, QueryDict):
            request.data._mutable = True
        request.data['space'] = space
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data,
                        status=status.HTTP_201_CREATED,
                        headers=headers)

    def perform_create(self, serializer):
        """Method to save serializer"""

        serializer.save()


class ViewRoom(mixins.ListModelMixin, generics.GenericAPIView):
    """This class defines the view behavior of the room."""
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    lookup_url_kwarg = "space"
    permission_classes = (
        permissions.IsAuthenticated,)

    def get_queryset(self):
        """Custom method to view rooms filtered by space"""
        space = self.kwargs.get(self.lookup_url_kwarg)
        rooms = Room.objects.filter(space=space)
        return rooms

    def get(self, request, *args, **kwargs):
        """Method to view all rooms"""
        return self.list(request, *args, **kwargs)


class UpdateRoom(mixins.UpdateModelMixin, generics.GenericAPIView):
    """This class defines the update  behavior of the room."""
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    lookup_url_kwarg = "space"

    permission_classes = (
        permissions.IsAuthenticated, IsFacilities)

    def put(self, request, *args, **kwargs):
        """Custom method to update rooms"""
        space = self.kwargs.get(self.lookup_url_kwarg)
        if isinstance(request.data, QueryDict):
            request.data._mutable = True
        request.data['space'] = space
        return self.update(request, *args, **kwargs)


class DeleteRoom(mixins.DestroyModelMixin, generics.GenericAPIView):
    """This class defines the delete behavior of the room."""
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (
        permissions.IsAuthenticated, IsFacilities)

    def delete(self, request, *args, **kwargs):
        """Method to delete a room"""
        return self.destroy(request, *args, **kwargs)


class RetrieveRoom(mixins.RetrieveModelMixin, generics.GenericAPIView):
    """This class defines the view behavior of the room."""
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (
        permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        """Method to retrieve a single room"""
        return self.retrieve(request, *args, **kwargs)


##################################################


class CreateOccupant(generics.CreateAPIView):
    """This class defines the create behavior of the occupant."""
    queryset = Occupant.objects.all()
    serializer_class = OccupantsSerializer
    lookup_url_kwarg = "room"
    permission_classes = (
        permissions.IsAuthenticated, IsFacilities)

    def create(self, request, *args, **kwargs):
        """Custom method to create occupants"""
        room = self.kwargs.get(self.lookup_url_kwarg)
        if isinstance(request.data, QueryDict):
            request.data._mutable = True
        request.data['room'] = room
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data,
                        status=status.HTTP_201_CREATED,
                        headers=headers)


class ViewOccupant(mixins.ListModelMixin, generics.GenericAPIView):
    """This class defines the view behavior of the occupants."""
    queryset = Occupant.objects.all()
    serializer_class = OccupantsSerializer
    permission_classes = (
        permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        """Custom view method that defines a get request for all items"""
        return self.list(request, *args, **kwargs)


class UpdateOccupant(mixins.UpdateModelMixin, generics.GenericAPIView):
    """This class defines the update  behavior of the occupant."""
    queryset = Occupant.objects.all()
    serializer_class = OccupantsSerializer
    permission_classes = (
        permissions.IsAuthenticated, IsFacilities)

    def put(self, request, *args, **kwargs):
        """Custom view method that defines a put request"""
        space = self.kwargs.get(self.lookup_url_kwarg)
        if isinstance(request.data, QueryDict):
            request.data._mutable = True
        request.data['space'] = space
        return self.update(request, *args, **kwargs)


class DeleteOccupant(mixins.DestroyModelMixin, generics.GenericAPIView):
    """This class defines the delete behavior of the occupant."""
    queryset = Occupant.objects.all()
    serializer_class = OccupantsSerializer
    permission_classes = (
        permissions.IsAuthenticated, IsFacilities)

    def delete(self, request, *args, **kwargs):
        """Custom view method that defines a delete request"""
        return self.destroy(request, *args, **kwargs)


class RetrieveOccupant(mixins.RetrieveModelMixin, generics.GenericAPIView):
    """This class defines the view behavior of the occupant."""
    queryset = Occupant.objects.all()
    serializer_class = OccupantsSerializer
    permission_classes = (
        permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        """Custom view method that defines a get request for single occupant"""
        return self.retrieve(request, *args, **kwargs)
