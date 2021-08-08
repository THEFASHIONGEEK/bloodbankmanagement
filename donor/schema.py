import graphene
from graphene_django.types import DjangoObjectType

from .models import Donor, BloodDonate

class DonorType(DjangoObjectType):
    class Meta:
        model = Donor
        field = '__all__'


class BloodDonateType(DjangoObjectType):
    class Meta:
        model = BloodDonate

class Query(graphene.ObjectType):
    all_Donor = graphene.List(DonorType)

schema = graphene.Schema(query=Query)


