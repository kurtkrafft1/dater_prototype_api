from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from daterapp.models import PastDate, DaterUser
from .firebase  import auth, firebase, db 
from .dater_users import DaterUserSerializer
from django.utils import timezone
from datetime import datetime


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
        firebase_user = auth.get_account_info(request.META['HTTP_AUTHORIZATION'])
        dates = PastDate.objects.all()
        all = self.request.query_params.get('all', None)
        if all is not None:
           dates = PastDate.objects.raw('''
                SELECT
                *
                from daterapp_pastdate 
                where UID =%s;
            ''', [firebase_user['users'][0]['localId']])
       

        else: 
           dates = dates.filter(UID = firebase_user['users'][0]['localId'])

        serializer = PastDateSerializer(dates, many=True, context={"request": request})
        return Response(serializer.data)
    

    def create(self, request):

        firebase_user = auth.get_account_info(request.META['HTTP_AUTHORIZATION'])

        newPastDate = PastDate()
        dUser = DaterUser.objects.get(UID=firebase_user['users'][0]['localId'])
        newPastDate.first_maps_id = request.data['first_maps_id']
        newPastDate.second_maps_id = request.data['second_maps_id']
        newPastDate.second_maps_id = request.data['second_maps_id']
        newPastDate.third_maps_id = request.data['third_maps_id']
        newPastDate.created_at = timezone.now()
        newPastDate.is_favorite = request.data['is_favorite']
        newPastDate.UID = firebase_user['users'][0]['localId']
        newPastDate.dater_user = dUser

        newPastDate.save()

        serializer = PastDateSerializer(newPastDate, many=False, context = {'request': request})
        return Response(serializer.data)

    def update(self, request, pk=None):
        date = PastDate.objects.get(pk=pk)
        if date.is_favorite == True:
            date.is_favorite = False
        else:
            date.is_favorite = True
        date.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk=None):
        '''handles delete product'''
        try:
            pd = PastDate.objects.get(pk=pk)    
            pd.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except pd.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




