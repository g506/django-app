import graphene
from user.models import *
from django.db.models import F
from framework.api.API_Exception import APIException
from graphql_jwt.decorators import login_required


class isOnlineObj(graphene.ObjectType):
    isOnline = graphene.Boolean()

    def resolve_isOnline(self, info):
        return self['isOnline']


class coinsResponseObj(graphene.ObjectType):
    id = graphene.String()
    success = graphene.String()
class updateCoin(graphene.Mutation):

    class Arguments:
        coins = graphene.Int()

    Output = coinsResponseObj

    def mutate(self, info, coins=None):
        user = info.context.user
        coin = user.coins
        print(coin)

        if coins is not None:
            user.coins = coins + coin

        user.save()
        return coinsResponseObj(id=user.id, success = "True")


class Mutation(graphene.ObjectType):
    updateCoin = updateCoin.Field()


class Query(graphene.ObjectType):
    isOnline = graphene.List(isOnlineObj)


    def resolve_isOnline(self, info):
        print(User.objects.values().all())
        return User.objects.values().all()
