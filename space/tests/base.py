from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import Group
from accounts.models import User
from rest_framework.test import APIClient


class BaseTestCase(TestCase):
    """This class defines the test suite for the permissions. """

    def add_user_to_group(self, group, user):
        """Method to add user to group each with different permissions"""
        new_group = Group.objects.get(name=group)
        new_group.user_set.add(user)

    def create_groups(self):
        """Method to create user groups"""
        group = Group(name='Facilities')
        group.save()

        group = Group(name='Fellows')
        group.save()

        group = Group(name='Occupants')
        group.save()

        group = Group(name='Finance')
        group.save()

        group = Group(name='P&C')
        group.save()

    def assign_user_to_group(self):
        """Define the test client and other test variables."""
        self.create_groups()

        # assign users to different groups
        # Facilities
        self.facilities_manager = User.objects.create(
            username="user0", google_id=1)
        self.add_user_to_group('Facilities', self.facilities_manager)

        # Fellows
        self.fellow = User.objects.create(
            username="user1", google_id=2)
        self.add_user_to_group('Fellows', self.fellow)

        # Finanace
        self.finance_user = User.objects.create(
            username="user2", google_id=3)
        self.add_user_to_group('Finance', self.finance_user)

        # Occupants
        self.occupant = User.objects.create(
            username="user3", google_id=4)
        self.add_user_to_group('Occupants', self.occupant)

        # P&C
        self.pnc = User.objects.create(
            username="user4", google_id=5)
        self.add_user_to_group('P&C', self.pnc)

    def get(self, status_code, client, url=None, params=None):
        """Custom method that defines a get request for all items"""
        response = client.get(
            reverse(url, kwargs=params), format="json")
        self.assertEqual(response.status_code, status_code)

    def retrieve(self, status_code, client, url=None, params=None):
        """Custom method that defines a get request for single item"""
        response = client.get(
            reverse(url,
                    kwargs=params), format="json")
        self.assertEqual(response.status_code, status_code)

    def put(self, status_code, client, url=None, params=None, edit_data=None):
        """Custom method that defines a put request"""
        res = client.put(
            reverse(url, kwargs=params),
            edit_data, format="json")
        self.assertEqual(res.status_code, status_code)

    def delete(self, satus_code, client, url=None, params=None):
        """Custom method that defines a delete request"""
        response = client.delete(
            reverse(url, kwargs=params),
            format='json',
            follow=True)
        self.assertEqual(response.status_code, satus_code)

    def post(self, data, client, url=None, params=None):
        """Custom method that defines a post request"""
        return client.post(
            reverse(url, kwargs=params),
            data,
            format="json")

    def user_authenticate(self):
        """Method to authenticate different types of users"""
        self.client = APIClient()
        self.client.force_authenticate(user=self.facilities_manager)
        self.client1 = APIClient()
        self.client1.force_authenticate(user=self.fellow)
        self.client2 = APIClient()
        self.client2.force_authenticate(user=self.finance_user)
        self.client3 = APIClient()
        self.client3.force_authenticate(user=self.occupant)
        self.client4 = APIClient()
        self.client4.force_authenticate(user=self.pnc)
