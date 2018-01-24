from django.db import models
from andela_facilities.models import Base
from accounts.models import User


# Create your models here.
class Space(Base):
    """This class represents the space model."""
    name = models.CharField(max_length=255, blank=False, unique=True)
    owner = models.ForeignKey(User, related_name=None,
                              on_delete=models.CASCADE)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)


class Room(Base):
    """This class represents the room model."""
    room_name = models.CharField(max_length=255, blank=False, unique=True)
    capacity = models.IntegerField(blank=False)
    space = models.ForeignKey(Space,
                              related_name='Space',
                              on_delete=models.CASCADE)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.room_name)


class Occupant(Base):
    """This class represents the occupant model."""
    entry_date = models.DateField()
    exit_date = models.DateField(blank=True, null=True)
    room = models.ForeignKey(Room,
                             related_name='Room',
                             on_delete=models.CASCADE)
    owner = models.ForeignKey(User, related_name=None,
                              on_delete=models.CASCADE)
