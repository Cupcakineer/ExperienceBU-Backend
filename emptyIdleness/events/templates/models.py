from django.db import models
from django.utils import timezone

class Event (models.Model):
    eventID = models.CharField(max_length=20)
    title = models.CharField(max_length = 120) #length of title
    content = models.TextField()
    date_posted = models.DateTimeField(default= timezone.now) #when post was created
    
