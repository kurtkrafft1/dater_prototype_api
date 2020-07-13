from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from daterapp.models import DaterUser
from .firebase import firebase, auth, db

class DaterUserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = DaterUser
        url = serializers.HyperlinkedIdentityField(
            view_name="dater_users",
            lookup_field = "id"
        )
        fields = ("id", "UID" )

class DaterUsers(ViewSet):

    def list(self, request):
        fbUser = self.request.query_params.get('user_info', None)
        if fbUser is not None:
            user = auth.get_account_info(request.META['HTTP_AUTHORIZATION'])
            name = db.child("users").child(user['users'][0]['localId']).child("details").get()
            return Response(name.val())
            
        else:
            users = DaterUser.objects.all()
            serializer = DaterUserSerializer(users, many=True, context = {"request": request})
            return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
                user = DaterUser.objects.get(pk=pk)
                serializer = DaterUserSerializer(user, many=False, context={"request":request})

                return Response(serializer.data)

        except Exception as ex:

            return HttpResponseServerError(ex)