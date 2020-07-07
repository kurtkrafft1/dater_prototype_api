from django.db import models
''' a model that will represent different date options '''

class DateOption(models.Model):
    '''
    Arguments Required:
    name - varchar 
    '''

    name = models.CharField(max_length=55)
    
    class Meta:
        ordering = ('name',)