import graphene
from travel_log_data.models import *
from django.db.models import F
from framework.api.API_Exception import APIException
from graphql_jwt.decorators import login_required


class TransportObj(graphene.ObjectType):
    transport_id = graphene.String(required=True)
    transport_type = graphene.String(required=True)


    def resolve_transport_id(self, info):
        return self['id']

    def resolve_transport_type(self, info):
        return self['transport_type']

class ActivitiesObj(graphene.ObjectType):
    activity_id = graphene.String(required=True)
    activity_type = graphene.String(required=True)


    def resolve_activity_id(self, info):
        return self['id']

    def resolve_activity_type(self, info):
        return self['activity_type']

class LocationObj(graphene.ObjectType):
    location_name = graphene.String(required=True)
    location_id = graphene.String(required=True)
    location_latitude = graphene.String(required=True)
    location_longitude = graphene.String(required=True)
    location_country = graphene.String(required=True)
    location_currency = graphene.String(required=True)
    location_transports = graphene.List(TransportObj)
    location_activities = graphene.List(ActivitiesObj)

    def resolve_location_name(self, info):
        return self['location_name']
    
    def resolve_location_id(self, info):
        return self['id']
    
    def resolve_location_latitude(self, info):
        return self['location_latitude']

    def resolve_location_longitude(self, info):
        return self['location_longitude']

    def resolve_location_currency(self, info):
        return self['location_currency']

    #@graphene.resolve_only_args
    #def resolve_location_transports(self):
        #return Transport.objects.values().annotate(
        #   name=F('location_transports__name'),
        #).filter(id=self['id'])

    #def resolve_location_activities(self):
        #return Activities.objects.values().annotate(
            #name=F('activity_type__name'),
        #).filter(id=self['activity_id'])


class ReviewsObj(graphene.ObjectType):
    review_id = graphene.String(required=True)
    content = graphene.String(required=True)

    def resolve_review_id(self, info):
        return self['id']
    def resolve_content(self, info):
        return self['content']

class Query(graphene.ObjectType):
    locations = graphene.List(LocationObj)
    transports = graphene.List(TransportObj)
    activities = graphene.List(ActivitiesObj)
    reviews = graphene.List(ReviewsObj)

    def resolve_locations(self, info):
        return Location.objects.values().all()

    def resolve_transports(self, info):
        return Transport.objects.values().all()

    def resolve_activities(self, info):
        return Activities.objects.values().all()

    def resolve_reviews(self, info):
        return Reviews.objects.values().all()

schema = graphene.Schema(query=Query)