import secrets
import string
from datetime import datetime, timedelta
from framework import settings
import graphene
from django.contrib.auth import get_user_model
import travel_log_data.schema
import user.schema
import graphql_jwt
from .api.API_Exception import APIException
import graphene
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import login_required
from user.models import User

class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()

class userResponseObj(graphene.ObjectType):
    id = graphene.String()


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, username, password, email):
        user = get_user_model()(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()

        return CreateUser(user=user)

class UpdateProfile(graphene.Mutation):

    class Arguments:
        username = graphene.String()
        firstName = graphene.String()
        lastName = graphene.String()
        email = graphene.String()
        phoneNo = graphene.String()
        gender = graphene.String()
        bio = graphene.String()
        url = graphene.String()
        location = graphene.String()
        country = graphene.String()
        birthday = graphene.Date()
        avatar = graphene.String()
        isServiceProvider = graphene.Boolean()

    Output = userResponseObj

    def mutate(self, info, username=None, firstName=None, lastName=None, email=None,phoneNo=None,gender=None,
               bio=None,url=None,location=None,country=None,birthday=None,avatar=None,isServiceProvider=None):
        global socialObj
        user = info.context.user
        profile = info.context.user
        if username is not None:
            user.username = username
        if firstName is not None:
            user.first_name = firstName
            profile.first_name = firstName
        if lastName is not None:
            user.last_name = lastName
            profile.last_name = lastName
        if email is not None:
            user.email = email
            profile.email = email
        if phoneNo is not None:
            profile.phone = phoneNo
        if gender is not None:
            profile.gender = gender
        if bio is not None:
            profile.bio = bio
        if url is not None:
            profile.url = url
        if location is not None:
            profile.location = location
        if country is not None:
            profile.country = country
        if birthday is not None:
            profile.birthday = birthday
        if avatar is not None:
            profile.avatar = avatar
        if isServiceProvider is not None:
            profile.isServiceProvider = isServiceProvider
        user.save()
        profile.save()
        return userResponseObj(id=user.id)

class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    create_user = CreateUser.Field()
    updateProfile = UpdateProfile.Field()


class Query(
    travel_log_data.schema.Query,
    user.schema.Query,
    graphene.ObjectType):
    users = graphene.List(UserType)
    user = graphene.Field(UserType, username=graphene.String(required=True))

    def resolve_users(self, info):
        return get_user_model().objects.all()
        
    @staticmethod
    def resolve_user(self, info, **kwargs):
        username = kwargs.get('username')
        if username is not None:
            return get_user_model().objects.get(username=username)
        else:
            raise Exception('Username is a required parameter')


schema = graphene.Schema(query=Query, mutation=Mutation)