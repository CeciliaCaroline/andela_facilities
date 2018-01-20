from django.db import models


class Base(models.Model):
    """Base class containing information common to the models"""

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        """Define model as abstract"""
        abstract = True
