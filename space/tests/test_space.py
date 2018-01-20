from django.test import TestCase
from rest_framework import status
from django.contrib.auth.models import User
from space.models import Space
from .base import BaseTestCase


class SpaceModelTestCase(TestCase):
    """This class defines the test suite for the space model."""

    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create(username="nerd")
        self.space_name = "Space 1"
        self.space = Space(name=self.space_name, owner=user)

    def test_model_can_create_a_space(self):
        """Test the space model can create a space."""
        old_count = Space.objects.count()
        self.space.save()
        new_count = Space.objects.count()
        self.assertNotEqual(old_count, new_count)


class SpaceViewTestCase(BaseTestCase):
    """Test suite for the space views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.assign_user_to_group()
        self.user_authenticate()

        self.space_data = {'name': 'space 2',
                           'owner': self.facilities_manager.id}
        self.response = self.post(self.space_data, self.client, 'create')
        self.space = self.response.data

    def test_create_space_by_facilities(self):
        """Test the space can be created."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_get_space_by_facilities(self):
        """Test view to retrieve all spaces"""
        self.get(status.HTTP_200_OK, self.client, 'all_spaces')

    def test_update_space_by_facilities(self):
        """Test view to update space"""
        self.put(status.HTTP_200_OK, self.client,
                 'update', {'pk': self.space['id']}, {'name': 'spaces12'})

    def test_delete_space_by_facilities(self):
        """Test View can delete space"""
        self.delete(status.HTTP_204_NO_CONTENT,
                    self.client, 'delete', {'pk': self.space['id']})

    def test_single_space_by_facilities(self):
        """Test View can view single space"""
        self.retrieve(status.HTTP_200_OK, self.client,
                      'retrieve_space', {'pk': self.space['id']})

###########

    def test_create_space_by_fellow(self):
        """Test the space can be created."""
        res = self.post(self.space_data, self.client1, 'create')
        self.assertEqual(res.status_code,
                         status.HTTP_403_FORBIDDEN)

    def test_get_space_by_fellow(self):
        """Test view to retrieve all spaces"""
        self.get(status.HTTP_200_OK, self.client1, 'all_spaces')

    def test_update_space_by_fellow(self):
        """Test view to update space"""
        self.put(status.HTTP_403_FORBIDDEN, self.client1,
                 'update', {'pk': self.space['id']}, {'name': 'spaces12'})

    def test_delete_space_by_fellow(self):
        """Test View can delete space"""
        self.delete(status.HTTP_403_FORBIDDEN, self.client1,
                    'delete', {'pk': self.space['id']})

    def test_single_space_by_fellow(self):
        """Test View can view single space"""
        self.retrieve(status.HTTP_200_OK, self.client1,
                      'retrieve_space', {'pk': self.space['id']})

###########

    def test_create_space_by_finance(self):
        """Test the space can be created."""
        res = self.post(self.space_data, self.client2, 'create')
        self.assertEqual(res.status_code,
                         status.HTTP_403_FORBIDDEN)

    def test_get_space_by_finance(self):
        """Test view to retrieve all spaces"""
        self.get(status.HTTP_200_OK, self.client2, 'all_spaces')

    def test_update_space_by_finance(self):
        """Test view to update space"""
        self.put(status.HTTP_403_FORBIDDEN, self.client2,
                 'update', {'pk': self.space['id']}, {'name': 'spaces12'})

    def test_delete_space_by_finance(self):
        """Test View can delete space"""
        self.delete(status.HTTP_403_FORBIDDEN, self.client2,
                    'delete', {'pk': self.space['id']})

    def test_single_space_by_finance(self):
        """Test View can view single space"""
        self.retrieve(status.HTTP_200_OK, self.client2,
                      'retrieve_space', {'pk': self.space['id']})

###########

    def test_create_space_by_occupant(self):
        """Test the space can be created."""
        res = self.post(self.space_data, self.client3, 'create')
        self.assertEqual(res.status_code,
                         status.HTTP_403_FORBIDDEN)

    def test_get_space_by_occupant(self):
        """Test view to retrieve all spaces"""
        self.get(status.HTTP_200_OK, self.client3, 'all_spaces')

    def test_update_space_by_occupant(self):
        """Test view to update space"""
        self.put(status.HTTP_403_FORBIDDEN, self.client3,
                 'update', {'pk': self.space['id']}, {'name': 'spaces12'})

    def test_delete_space_by_occupant(self):
        """Test View can delete space"""
        self.delete(status.HTTP_403_FORBIDDEN, self.client3,
                    'delete', {'pk': self.space['id']})

    def test_single_space_by_occupant(self):
        """Test View can view single space"""
        self.retrieve(status.HTTP_200_OK, self.client3,
                      'retrieve_space', {'pk': self.space['id']})

###########

    def test_create_space_by_pnc(self):
        """Test the space can be created."""
        res = self.post(self.space_data, self.client4, 'create')
        self.assertEqual(res.status_code,
                         status.HTTP_403_FORBIDDEN)

    def test_get_space_by_pnc(self):
        """Test view to retrieve all spaces"""
        self.get(status.HTTP_200_OK, self.client4, 'all_spaces')

    def test_update_space_by_pnc(self):
        """Test view to update space"""
        self.put(status.HTTP_403_FORBIDDEN, self.client4,
                 'update', {'pk': self.space['id']}, {'name': 'spaces12'})

    def test_delete_space_by_pnc(self):
        """Test View can delete space"""
        self.delete(status.HTTP_403_FORBIDDEN, self.client4,
                    'delete', {'pk': self.space['id']})

    def test_single_space_by_pnc(self):
        """Test View can view single space"""
        self.retrieve(status.HTTP_200_OK, self.client4,
                      'retrieve_space', {'pk': self.space['id']})
