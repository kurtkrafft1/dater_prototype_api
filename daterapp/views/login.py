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

@csrf_exempt
def login_user(request):
    '''Handles the authentication of a user

    Method arguments:
      request -- The full HTTP request object
    '''
    # print(request)
    req_body = json.loads(request.body.decode())
    if request.method == 'POST':
      email = req_body["email"]
      password = req_body["password"]

      try:
          user = auth.sign_in_with_email_and_password(email,password)
          # print("EHEREREHASF", user.idToken)
          data = json.dumps({"valid": True, "token": user["idToken"]})
          return HttpResponse(data, content_type='application/json')
      except:
          data = json.dumps({"valid": False})
          return HttpResponse(data, content_type='application/json')