from django.db import models
from django.urls import reverse
from django.db.models import F

class DaterUser(models.Model):
    '''
    This class will join the firebase user to the rest of the database
    Arguments Required:
    UID Firebase User_id
    '''

    UID = models.CharField(max_length=129)

