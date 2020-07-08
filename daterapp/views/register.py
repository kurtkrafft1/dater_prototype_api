import pyrebase 
import json
from django.http import HttpResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from .firebase  import auth, firebase, db 

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

        data={"name":name, "birthdate": birthdate, "status": "1"}

        db.child('users').child(uid).child("details").set(data)

        http_data = json.dumps({"valid": True, "token": user["idToken"]})

        return HttpResponse(http_data, content_type='application/json')

      except:
          data = json.dumps({"valid": False})
          return HttpResponse(data, content_type='application/json')
      