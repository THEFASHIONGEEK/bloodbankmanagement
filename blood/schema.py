import graphene
from graphene_django.types import DjangoObjectType

from .models import Stock, BloodRequest

class StockType(DjangoObjectType):
    class Meta:
        model = Stock
        field = '__all__'


class BloodRequestType(DjangoObjectType):
    class Meta:
        model = BloodRequest

class Query(graphene.ObjectType):
    all_Stock = graphene.List(StockType)

schema = graphene.Schema(query=Query)


