from rest_framework import serializers
from .models import Space, Room, Occupant


class SpaceSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Space
        fields = ('id', 'name', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')


class RoomSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the room model fields"""
        model = Room
        fields = ('id', 'room_name',
                  'capacity', 'space', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')


class OccupantsSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the room model fields"""
        model = Occupant
        fields = ('id', 'entry_date', 'exit_date',
                  'room', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
