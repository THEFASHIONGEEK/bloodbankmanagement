import graphene
from graphene_django.types import DjangoObjectType

from .models import Patient

class PatientType(DjangoObjectType):
    class Meta:
        model = Patient
        field = '__all__'

class Query(graphene.ObjectType):
    all_Patient = graphene.List(PatientType)

schema = graphene.Schema(query=Query)