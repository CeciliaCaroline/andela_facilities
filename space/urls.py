from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (CreateView, ViewSpace, UpdateSpace,
                    RetrieveSpace, DeleteSpace, CreateRoom, ViewRoom,
                    UpdateRoom, DeleteRoom, RetrieveRoom, CreateOccupant,
                    UpdateOccupant, DeleteOccupant, RetrieveOccupant,
                    ViewOccupant)


urlpatterns = [
    path('create/', CreateView.as_view(), name="create"),
    path('', ViewSpace.as_view(), name='all_spaces'),
    path('<int:pk>/',
         RetrieveSpace.as_view(), name="retrieve_space"),
    path('edit/<int:pk>',
         UpdateSpace.as_view(), name='update'),
    path('delete/<int:pk>',
         DeleteSpace.as_view(), name='delete'),
    #######

    path('<int:space>/room/', include([
        path('create/',
             CreateRoom.as_view(), name="create_room"),
        path('<int:pk>/',
             RetrieveRoom.as_view(), name="retrieve_room"),
        path('', ViewRoom.as_view(), name='all_rooms'),
        path('edit/<int:pk>',
             UpdateRoom.as_view(), name='update_room'),
        path('delete/<int:pk>',
             DeleteRoom.as_view(), name='delete_room'),

        ########

        path('<int:room>/occupants/', include([
            path('create/',
                 CreateOccupant.as_view(), name="create_occupant"),
            path('<int:pk>/',
                 RetrieveOccupant.as_view(), name="retrieve_occupant"),
            path('edit/<int:pk>',
                 UpdateOccupant.as_view(), name='update_occupant'),
            path('delete/<int:pk>',
                 DeleteOccupant.as_view(), name='delete_occupant'),
            path('', ViewOccupant.as_view(), name="all_occupants"),
        ]))
    ]))
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])
