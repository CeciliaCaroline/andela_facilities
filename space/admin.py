from django.contrib import admin
from space.models import Space, Room, Occupant

# Register your models here.
admin.site.register(Space)
admin.site.register(Room)
admin.site.register(Occupant)
