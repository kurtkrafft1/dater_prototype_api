import pyrebase 
import json
from django.http import HttpResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from .firebase import auth, firebase, db 

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
          # data = json.dumps({"valid": True, "token": user["idToken"]})
          data = json.dumps({"valid": True, "token": user})
          return HttpResponse(data, content_type='application/json')
      except:
          data = json.dumps({"valid": False})
          return HttpResponse(data, content_type='application/json')