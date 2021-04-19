import graphene
from user.models import *
from django.db.models import F
from framework.api.API_Exception import APIException
from graphql_jwt.decorators import login_required

class FollowObj(graphene.ObjectType):
    followers = graphene.Int(required=True)
    followings = graphene.Int(required=True)
    username = graphene.String(required=True)

    def resolve_followers(self, info):
        return self['followers']

    def resolve_followings(self, info):
        return self['followings']

    def resolve_username(self, info):
        return User.objects.values().get(id=self['username_id'])

class RatingsObj(graphene.ObjectType):
    username = graphene.String(required=True)
    ratings = graphene.String(required=True)

    def resolve_ratings(self, info):
        return self['ratings']

    def resolve_username(self, info):
        return User.objects.values().get(id=self['username_id'])

class Query(graphene.ObjectType):
    follow = graphene.List(FollowObj)
    ratings = graphene.List(RatingsObj)

    def resolve_follow(self, info):
        return Follow.objects.values().all()
    
    def resolve_ratings(self, info):
        return Ratings.objects.values().all()

