from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from daterapp.models import PastDate
from .firebase  import auth, firebase, db 
from .dater_users import DaterUserSerializer


class PastDateSerializer(serializers.HyperlinkedModelSerializer):
    ''' 
        We nest the DaterUserSerializer here so we can have an accurate depth and not see an dateruser-detail error because 
        in the router we defined it as plural
    '''


    dater_user = DaterUserSerializer('dater_user')

    class Meta:
        model = PastDate

        url = serializers.HyperlinkedIdentityField(
            view_name="past_dates",
            lookup_field="id"
        )
        fields = ("id", "UID", "dater_user", "first_maps_id", "second_maps_id", "third_maps_id", "created_at", "is_favorite", "deleted")
        depth = 1

class PastDates(ViewSet):

    def list(self,request):
        '''
            This gets a little confusing here. So we are using Firebase Authentication for users so their data is private and can't be accessed 
            through this app. So we have to get the IdToken that was supplied to us by google pyrebase from the headers. BUT We can't user normal
            Authorization: Token {Token Here} because that will cast an invalid token error because it is expecting a Django Token 
            so we need to then use Request.META to get the HTTP defined Token which is the firebase token. Then we filter by that UID which 
            was requested from firebase. 

        '''

        firebase_user = auth.get_account_info(request.META['HTTP_TOKEN'])
        
        dates = PastDate.objects.all()
        by_user_dates = dates.filter(UID = firebase_user['users'][0]['localId'])
        serializer = PastDateSerializer(by_user_dates, many=True, context={"request": request})
        return Response(serializer.data)

