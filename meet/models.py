from py2neo.ogm import GraphObject, Property, Label, Related, RelatedTo
from people.models import Person


class Category(GraphObject):
    __primarykey__ = "name"

    category = Label("Category")

    name = Property()
    description = Property()

    room = RelatedTo("Room", "HAS_CATEGORY")

    def __str__(self):
        return f'{self.name}'


class RoomDetail(GraphObject):
    __primarykey__ = "room"

    room_detail = Label("RoomDetail")

    seat_count = Property()
    white_board = Property()
    projector = Property()
    date_updated = Property('updatedOn')

    room = RelatedTo("Room", "HAS_DETAIL")


class Room(GraphObject):
    __primarykey__ = "name"

    room = Label("Room")

    name = Property()
    detail = RelatedTo("RoomDetail")
    date_updated = Property('updatedOn')

    category = RelatedTo("Category", "HAS_CATEGORY")


class Event(GraphObject):
    appointment = Label("Appointment")
    
    name = Property()
    subject = Property()
    agender = Property()
    start_date = Property('startsOn')
    end_date = Property('endsOn')
    
    organizer = Related(Person)
    attendee = RelatedTo(Person)
    room = Related(Room)
    date_updated = Property('updatedOn')
