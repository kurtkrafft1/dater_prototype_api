import pyrebase 
#Just the firebase configuration


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