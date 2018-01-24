from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    google_id = models.CharField(max_length=60, unique=True)
    appuser_picture = models.TextField()

    # class Meta:
    #     abstract = True

    def check_diff(self, idinfo):
        """
        Check for differences between request/idinfo and model data.
            Args:
                idinfo: data passed in from post method.
        """
        data = {
                "username": idinfo['name'],
                "email": idinfo["email"],
                "first_name": idinfo['given_name'],
                "last_name": idinfo['family_name']
            }

        for field in data:
            if getattr(self, field) != data[field] and data[field] != '':
                setattr(self, field, data[field])
        self.save()
