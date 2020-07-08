import pyrebase 
import json
from django.http import HttpResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt


config = {
    "apiKey": "AIzaSyCzvwzt_1Hq7n10rEVBAZ0dmHtsz0_4CrI",
    "authDomain": "dater-385dc.firebaseapp.com",
    "databaseURL": "https://dater-385dc.firebaseio.com",
    "projectId": "dater-385dc",
    "storageBucket": "dater-385dc.appspot.com",
    "messagingSenderId": "327978469990",
    "appId": "1:327978469990:web:f3eb2cc59f544d84e9bba7",
    "measurementId": "G-L06SK2997T"
  }



firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

@csrf_exempt
def register_user(request):
    '''Handles the creation of a new user for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    req_body = json.loads(request.body.decode())
    if request.method == 'POST':
      email = req_body["email"]
      password = req_body["password"]
      name = req_body["name"]
      birthdate = req_body["birthdate"]
      try:
        user = auth.create_user_with_email_and_password(email, password)

        uid = user['localId']

        data={"name":name, "birthdate": birthdate}

        db.child('users').child(uid).child("details").set(data)

        http_data = json.dumps({"valid": True, "token": user["idToken"]})

        return HttpResponse(http_data, content_type='application/json')

      except:
          data = json.dumps({"valid": False})
          return HttpResponse(data, content_type='application/json')
      