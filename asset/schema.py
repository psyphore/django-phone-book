import graphene
from graphene_django.types import DjangoObjectType
from .models import Asset

class AssetType(DjangoObjectType):
    class Meta:
        model = Asset

class Query(graphene.ObjectType):
    all_assets = graphene.List(AssetType)