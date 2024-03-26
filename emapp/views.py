
# Create your views here.
from django.shortcuts import render
import pyrebase

config={
  "apiKey": "AIzaSyBmK-3-EHeqx5uG7z9tnkUjfWegg3_xOzg",
  "authDomain": "djangoapp-a0dde.firebaseapp.com",
  "databaseURL": "https://djangoapp-a0dde-default-rtdb.firebaseio.com",
  "projectId": "djangoapp-a0dde",
  "storageBucket": "djangoapp-a0dde.appspot.com",
  "messagingSenderId": "148921615797",
  "appId": "1:148921615797:web:d2f528c9fd23750b3f85fc",}
firebase=pyrebase.initialize_app(config)
authe=firebase.auth()
database=firebase.database()
# Create your views here.
def index(request):
    Current=database.child('PZEM').child('current').get().val()
    Energy=database.child('PZEM').child('energy').get().val()
    Frequency=database.child('PZEM').child('frequency').get().val()
    Power_Factor=database.child('PZEM').child('pf').get().val()
    Voltage=database.child('PZEM').child('voltage').get().val()
    Power=database.child('PZEM').child('power').get().val()
    return render(request, 'index.html',{
        "current":Current,
        "energy":Energy,
        "frequency":Frequency,
        "pf":Power_Factor,
        "voltage":Voltage,
        "power":Power
    })

# Create your views here.
