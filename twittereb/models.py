from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class tw_tweet(models.Model):
    parent_tweet_id = models.IntegerField(blank=True,null=True)
    name = models.CharField(max_length =100)
    text = models.CharField(max_length =250)
    image_path = models.CharField(max_length=100,blank=True, null=True)
    created_at = models.DateTimeField()
   
