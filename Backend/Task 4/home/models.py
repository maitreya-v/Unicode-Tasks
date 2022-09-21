from multiprocessing.sharedctypes import Value
from typing import Counter
from django.db import models
# Create your models here.
class ApiVal(models.Model):
    apicountry=models.CharField(max_length=122)
    apiiso2=models.CharField(max_length=122)
    apislug=models.CharField(max_length=122)
    counter=models.PositiveSmallIntegerField(max_length=50)
    
    def __str__(self):
        z=str(self.counter)+" "+self.apicountry
        return z