import graphene

from graphene_django.types import DjangoObjectType
from .models import Category, Room, RoomDetail, Event
from .service import MeetService


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class RoomType(DjangoObjectType):
    class Meta:
        model = Room


class RoomDetailType(DjangoObjectType):
    class Meta:
        model = RoomDetail


class EventType(DjangoObjectType):
    class Meta:
        model = Event


class MeetQuery(object):
    def __init__(self, *args, **kwargs):
        self.service = MeetService()

    category = graphene.Field(
        CategoryType, id=graphene.Int(), name=graphene.String())
    all_categories = graphene.List(CategoryType)
    room = graphene.Field(RoomType, id=graphene.Int(), name=graphene.String())
    all_rooms = graphene.List(RoomType)
    event = graphene.Field(EventType, id=graphene.Int(),
                           name=graphene.String())
    all_events = graphene.List(EventType)

    def resolve_all_categories(self, info, **kwargs):
        # return Category.objects.all()
        return self.service.get_all_categories(info, kwargs)

    def resolve_all_rooms(self, info, **kwargs):
        # return Room.object.select_related('category').all()
        pass

    def resolve_category(self, info, **kwargs):
        # id = kwargs.get('id')
        # name = kwargs.get('name')

        # if id is not None:
        #     return Category.objects.get(pk=id)

        # if name is not None:
        #     return Category.objects.get(name=name)

        # return None
        pass

    def resolve_room(self, info, **kwargs):
        # id = kwargs.get('id')
        # name = kwargs.get('name')

        # if id is not None:
        #     return Room.objects.get(pk=id)

        # if name is not None:
        #     return Room.objects.get(name=name)

        # return None
        pass
