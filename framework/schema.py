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


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


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

class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    create_user = CreateUser.Field()

class Query(
    travel_log_data.schema.Query,
    user.schema.Query,
    graphene.ObjectType):
    users = graphene.List(UserType)

    def resolve_users(self, info):
        return get_user_model().objects.all()

schema = graphene.Schema(query=Query, mutation=Mutation)