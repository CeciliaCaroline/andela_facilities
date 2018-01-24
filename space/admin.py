from django.contrib import admin
from space.models import Space, Room, Occupant
from accounts.models import User


# Register your models here.
admin.site.register(Space)
admin.site.register(Room)
admin.site.register(Occupant)
admin.site.register(User)
