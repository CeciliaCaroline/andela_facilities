from django.test import TestCase
from rest_framework import status
from accounts.models import User
from space.models import Space, Room
from .base import BaseTestCase


class RoomModelTestCase(TestCase):
    """This class defines the test suite for the space model."""
    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create(username="nerd", google_id=7)
        space = Space(name='Space 1', owner=user)
        space.save()
        self.room_name = "Room 1"
        self.room = Room(room_name=self.room_name, capacity=4, space=space)

    def test_model_can_create_a_room(self):
        """Test the space model can create a room."""
        old_count = Room.objects.count()
        self.room.save()
        new_count = Room.objects.count()
        self.assertNotEqual(old_count, new_count)


class RoomViewTestCase(BaseTestCase):
    """Test Suite for room views"""

    def setUp(self):
        """Define the test client and other test variables."""
        self.assign_user_to_group()
        self.user_authenticate()
        self.space_data = {'name': 'space 2',
                           'owner': self.facilities_manager.id}
        self.response = self.post(self.space_data, self.client, 'create')
        self.space = self.response.data['id']

        self.room_data = {'room_name': 'room1', 'capacity': 4,
                          'space': 1}

        self.res = self.post(self.room_data, self.client,
                             "create_room", {'space': self.space})
        self.room = self.res.data

    def test_create_room_by_facilities(self):
        """Test the room can be created."""
        self.assertEqual(self.res.status_code, status.HTTP_201_CREATED)

    def test_get_room_by_facilities(self):
        """Test view to retrieve all rooms"""
        self.get(status.HTTP_200_OK, self.client,
                 'all_rooms', {'space': self.space})

    def test_update_room_by_facilities(self):
        """Test view to update room"""
        self.put(status.HTTP_200_OK, self.client,
                 'update_room', {'pk': self.room['id'], 'space': self.space},
                 {'room_name': 'room11', 'capacity': 4})

    def test_delete_room_by_facilities(self):
        """Test View can delete room"""
        self.delete(status.HTTP_204_NO_CONTENT,
                    self.client, 'delete_room',
                    {'pk': self.room['id'], 'space': self.space})

    def test_single_room_by_facilities(self):
        """Test View can view single room"""
        self.retrieve(status.HTTP_200_OK, self.client,
                      "retrieve_room",
                      {'pk': self.room['id'], 'space': self.space})

###########

    def test_create_room_by_fellow(self):
        """Test the room can be created."""
        self.res = self.post(self.room_data, self.client1,
                             "create_room", {'space': self.space})
        self.assertEqual(self.res.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_room_by_fellow(self):
        """Test view to retrieve all rooms"""
        self.get(status.HTTP_200_OK, self.client1,
                 'all_rooms', {'space': self.space})

    def test_update_room_by_fellow(self):
        """Test view to update room"""
        self.put(status.HTTP_403_FORBIDDEN, self.client1,
                 'update_room', {'pk': self.room['id'], 'space': self.space},
                 {'room_name': 'room11', 'capacity': 4})

    def test_delete_room_by_fellow(self):
        """Test View can delete room"""
        self.delete(status.HTTP_403_FORBIDDEN,
                    self.client1, 'delete_room',
                    {'pk': self.room['id'], 'space': self.space})

    def test_single_room_by_fellow(self):
        """Test View can view single room"""
        self.retrieve(status.HTTP_200_OK, self.client1,
                      "retrieve_room",
                      {'pk': self.room['id'], 'space': self.space})

###########

    def test_create_room_by_finance(self):
        """Test the room can be created."""
        self.res = self.post(self.room_data, self.client2,
                             "create_room", {'space': self.space})
        self.assertEqual(self.res.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_room_by_finance(self):
        """Test view to retrieve all rooms"""
        self.get(status.HTTP_200_OK, self.client2,
                 'all_rooms', {'space': self.space})

    def test_update_room_by_finance(self):
        """Test view to update room"""
        self.put(status.HTTP_403_FORBIDDEN, self.client2,
                 'update_room', {'pk': self.room['id'], 'space': self.space},
                 {'room_name': 'room11', 'capacity': 4})

    def test_delete_room_by_finance(self):
        """Test View can delete room"""
        self.delete(status.HTTP_403_FORBIDDEN,
                    self.client2, 'delete_room',
                    {'pk': self.room['id'], 'space': self.space})

    def test_single_room_by_finance(self):
        """Test View can view single room"""
        self.retrieve(status.HTTP_200_OK, self.client2,
                      "retrieve_room",
                      {'pk': self.room['id'], 'space': self.space})

###########

    def test_create_room_by_occupant(self):
        """Test the room can be created."""
        self.res = self.post(self.room_data, self.client3,
                             "create_room", {'space': self.space})
        self.assertEqual(self.res.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_room_by_occupant(self):
        """Test view to retrieve all rooms"""
        self.get(status.HTTP_200_OK, self.client3,
                 'all_rooms', {'space': self.space})

    def test_update_room_by_occupant(self):
        """Test view to update room"""
        self.put(status.HTTP_403_FORBIDDEN, self.client3,
                 'update_room', {'pk': self.room['id'], 'space': self.space},
                 {'room_name': 'room11', 'capacity': 4})

    def test_delete_room_by_occupant(self):
        """Test View can delete room"""
        self.delete(status.HTTP_403_FORBIDDEN,
                    self.client3, 'delete_room',
                    {'pk': self.room['id'], 'space': self.space})

    def test_single_room_by_occupant(self):
        """Test View can view single room"""
        self.retrieve(status.HTTP_200_OK, self.client3,
                      "retrieve_room",
                      {'pk': self.room['id'], 'space': self.space})

###########

    def test_create_room_by_pnc(self):
        """Test the room can be created."""
        self.res = self.post(self.room_data, self.client4,
                             "create_room", {'space': self.space})
        self.assertEqual(self.res.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_room_by_pnc(self):
        """Test view to retrieve all rooms"""
        self.get(status.HTTP_200_OK, self.client4,
                 'all_rooms', {'space': self.space})

    def test_update_room_by_pnc(self):
        """Test view to update room"""
        self.put(status.HTTP_403_FORBIDDEN, self.client4,
                 'update_room', {'pk': self.room['id'], 'space': self.space},
                 {'room_name': 'room11', 'capacity': 4})

    def test_delete_room_by_pnc(self):
        """Test View can delete room"""
        self.delete(status.HTTP_403_FORBIDDEN,
                    self.client4, 'delete_room',
                    {'pk': self.room['id'], 'space': self.space})

    def test_single_room_by_pnc(self):
        """Test View can view single room"""
        self.retrieve(status.HTTP_200_OK, self.client4,
                      "retrieve_room",
                      {'pk': self.room['id'], 'space': self.space})
