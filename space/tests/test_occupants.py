from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from accounts.models import User
from space.models import Space, Room, Occupant
from .base import BaseTestCase


class OccupantModelTestCase(TestCase):
    """This class defines the test suite for the occupant model."""
    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create(username="nerd", google_id=8)
        space = Space(name='Space 1', owner=user)
        space.save()
        room = Room(room_name="Room 1", capacity=4, space=space)
        room.save()
        entry_date = '2017-01-01'
        self.occupant = Occupant(entry_date=entry_date,
                                 exit_date=None, room=room, owner=user)

    def test_model_can_create_occupant(self):
        """Test the space model can create an occupant."""
        old_count = Occupant.objects.count()
        self.occupant.save()
        new_count = Occupant.objects.count()
        self.assertNotEqual(old_count, new_count)


class OccupantViewTestCase(BaseTestCase):
    """This class defines the test suite for the occupant views"""

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
        self.room = self.res.data['id']

        self.occupant_data = {'entry_date': '2017-01-01',
                              'exit_date': '2017-06-06', 'room': self.room,
                              'owner': self.facilities_manager.id}
        self.resp = self.post(self.occupant_data,
                              self.client, "create_occupant",
                              {'space': self.space, 'room': self.room})
        self.occupant_response = self.resp.data

    def test_create_occupant_facilities(self):
        """Test the occupant can be created."""
        self.assertEqual(self.resp.status_code, status.HTTP_201_CREATED)

    def test_get_occupant_by_facilities(self):
        """Test view to retrieve all occupants"""
        self.get(status.HTTP_200_OK, self.client,
                 "all_occupants", {'space': self.space, 'room': self.room})

    def test_update_occupant_facilities(self):
        """Test view to update occupant"""
        self.put(status.HTTP_200_OK, self.client,
                 'update_occupant',
                 {'pk': self.occupant_response['id'],
                  'space': self.space, 'room': self.room},
                 {'entry_date': '2017-01-01', 'exit_date': '2017-06-07',
                  'room': self.room, 'owner': self.facilities_manager.id})

    def test_delete_occupant_facilities(self):
        """Test View can delete occupant"""
        self.delete(status.HTTP_204_NO_CONTENT,
                    self.client, 'delete_occupant',
                    {'pk': self.occupant_response['id'],
                     'space': self.space, 'room': self.room})

    def test_single_occupant_facilities(self):
        """Test View can view single occupant"""
        self.retrieve(status.HTTP_200_OK, self.client,
                      "retrieve_occupant",
                      {'pk': self.occupant_response['id'],
                       'space': self.space, 'room': self.room})

###########

    def test_create_occupant_fellow(self):
        """Test the occupant can be created."""
        self. resp = self.post(self.occupant_data,
                               self.client1, "create_occupant",
                               {'space': self.space, 'room': self.room})
        self.assertEqual(self.resp.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_occupant_by_fellow(self):
        """Test view to retrieve all occupants"""
        self.get(status.HTTP_200_OK, self.client1,
                 "all_occupants", {'space': self.space, 'room': self.room})

    def test_update_occupant_fellow(self):
        """Test view to update occupant"""
        self.put(status.HTTP_403_FORBIDDEN,
                 self.client1, 'update_occupant',
                 {'pk': self.occupant_response['id'],
                  'space': self.space, 'room': self.room},
                 {'entry_date': '2017-01-01', 'exit_date': '2017-06-07',
                  'room': self.room, 'owner': self.facilities_manager.id})

    def test_delete_occupant_fellow(self):
        """Test View can delete occupant"""
        self.delete(status.HTTP_403_FORBIDDEN,
                    self.client1, 'delete_occupant',
                    {'pk': self.occupant_response['id'],
                     'space': self.space, 'room': self.room})

    def test_single_occupant_fellow(self):
        """Test View can view single occupant"""
        self.retrieve(status.HTTP_200_OK, self.client1,
                      "retrieve_occupant",
                      {'pk': self.occupant_response['id'],
                       'space': self.space, 'room': self.room})

###########

    def test_create_occupant_finance(self):
        """Test the occupant can be created."""
        self. resp = self.post(self.occupant_data,
                               self.client2, "create_occupant",
                               {'space': self.space, 'room': self.room})
        self.assertEqual(self.resp.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_occupant_by_finance(self):
        """Test view to retrieve all occupants"""
        self.get(status.HTTP_200_OK, self.client2,
                 "all_occupants", {'space': self.space, 'room': self.room})

    def test_update_occupant_finance(self):
        """Test view to update occupant"""
        self.put(status.HTTP_403_FORBIDDEN,
                 self.client2, 'update_occupant',
                 {'pk': self.occupant_response['id'],
                  'space': self.space, 'room': self.room},
                 {'entry_date': '2017-01-01', 'exit_date': '2017-06-07',
                  'room': self.room, 'owner': self.facilities_manager.id})

    def test_delete_occupant_finance(self):
        """Test View can delete occupant"""
        self.delete(status.HTTP_403_FORBIDDEN,
                    self.client2, 'delete_occupant',
                    {'pk': self.occupant_response['id'],
                     'space': self.space, 'room': self.room})

    def test_single_occupant_finance(self):
        """Test View can view single occupant"""
        self.retrieve(status.HTTP_200_OK, self.client2,
                      "retrieve_occupant",
                      {'pk': self.occupant_response['id'],
                       'space': self.space, 'room': self.room})

###########

    def test_occupant_create_occupant(self):
        """Test the occupant can be created."""
        self. resp = self.post(self.occupant_data,
                               self.client3, "create_occupant",
                               {'space': self.space, 'room': self.room})
        self.assertEqual(self.resp.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_occupant_by_occupant(self):
        """Test view to retrieve all occupants"""
        self.get(status.HTTP_200_OK, self.client3,
                 "all_occupants", {'space': self.space, 'room': self.room})

    def test_occupant_update_occupant(self):
        """Test view to update occupant"""
        self.put(status.HTTP_403_FORBIDDEN,
                 self.client3, 'update_occupant',
                 {'pk': self.occupant_response['id'],
                  'space': self.space, 'room': self.room},
                 {'entry_date': '2017-01-01', 'exit_date': '2017-06-07',
                  'room': self.room, 'owner': self.facilities_manager.id})

    def test_delete_occupant(self):
        """Test View can delete occupant"""
        self.delete(status.HTTP_403_FORBIDDEN,
                    self.client3, 'delete_occupant',
                    {'pk': self.occupant_response['id'],
                     'space': self.space, 'room': self.room})

    def test_single_occupant(self):
        """Test View can view single occupant"""
        self.retrieve(status.HTTP_200_OK, self.client3,
                      "retrieve_occupant",
                      {'pk': self.occupant_response['id'],
                       'space': self.space, 'room': self.room})

###########

    def test_create_occupant_pnc(self):
        """Test the occupant can be created."""
        self. resp = self.post(self.occupant_data,
                               self.client4, "create_occupant",
                               {'space': self.space, 'room': self.room})
        self.assertEqual(self.resp.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_occupant_by_pnc(self):
        """Test view to retrieve all occupants"""
        self.get(status.HTTP_200_OK, self.client4,
                 "all_occupants", {'space': self.space, 'room': self.room})

    def test_update_occupant_pnc(self):
        """Test view to update occupant"""
        self.put(status.HTTP_403_FORBIDDEN,
                 self.client4, 'update_occupant',
                 {'pk': self.occupant_response['id'],
                  'space': self.space, 'room': self.room},
                 {'entry_date': '2017-01-01', 'exit_date': '2017-06-07',
                  'room': self.room, 'owner': self.facilities_manager.id})

    def test_delete_occupant_pnc(self):
        """Test View can delete occupant"""
        self.delete(status.HTTP_403_FORBIDDEN,
                    self.client4, 'delete_occupant',
                    {'pk': self.occupant_response['id'],
                     'space': self.space, 'room': self.room})

    def test_single_occupant_pnc(self):
        """Test View can view single occupant"""
        self.retrieve(status.HTTP_200_OK, self.client4,
                      "retrieve_occupant",
                      {'pk': self.occupant_response['id'],
                       'space': self.space, 'room': self.room})
