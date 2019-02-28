from django.conf import settings

import graphene
from graphene_django.debug import DjangoDebug

from crm.meet.schema import MeetQueries, MeetMutations
from crm.asset.schema import AssetQueries, AssetMutations
from crm.person.schema import PersonQueries, PersonMutations

class Query(MeetQueries, AssetQueries, PersonQueries, graphene.ObjectType):
    if settings.DEBUG:
        # Debug output - see
        # http://docs.graphene-python.org/projects/django/en/latest/debug/
        debug = graphene.Field(DjangoDebug, name='__debug')

class Mutation(MeetMutations, AssetMutations, PersonMutations, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)