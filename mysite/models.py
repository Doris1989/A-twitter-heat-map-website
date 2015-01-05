from django.db import models
import string



class Tweet(models.Model):
    user = models.BigIntegerField()
    tid = models.BigIntegerField(primary_key=True)
    lat = models.FloatField()
    lon = models.FloatField()
    text = models.TextField(max_length=256)
    time = models.DateField()
    kwd = models.CharField(max_length=50)