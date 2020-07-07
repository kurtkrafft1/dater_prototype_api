from django.db import models
from django.db.models import F
from daterapp.models import DaterUser
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE

class PastDate(SafeDeleteModel):
    '''

    Arguments Required:
    UID foreign key from the DUser table (thus the firebase table)
    first_maps_id string representing the place_id from google maps API
    second_maps_id string representing the place_id from google maps API
    third_maps_id string representing the place_id from google maps API
    created_at date_time
    favorited boolean value
    '''
    _safedelete_policy = SOFT_DELETE
    '''doesn't delete old dates, just archive them'''

    dater_user = models.ForeignKey(DaterUser, on_delete=models.DO_NOTHING)
    first_maps_id = models.CharField(max_length=155)
    second_maps_id = models.CharField(max_length=155)
    third_maps_id = models.CharField(max_length=155)
    created_at = models.DateTimeField()
    is_favorite = models.BooleanField()

    class Meta:
        ordering = (F('created_at').desc(nulls_last=True),)