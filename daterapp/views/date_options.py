from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from daterapp.models import DateOption
#used to return a master list of all possible date options ordered by name (see line 24)


class DateOptionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = DateOption
        url = serializers.HyperlinkedIdentityField(
            view_name="date_options",
            lookup_field = "id"
        )
        fields = ("id", "name")

class DateOptions(ViewSet):

    def list(self, request):

        options = DateOption.objects.order_by("name")
        serializer = DateOptionSerializer(options, many=True, context={"request": request})

        return Response(serializer.data)