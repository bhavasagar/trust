from django.db.models.signals import post_save,pre_save
from django.conf import settings
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models import Sum
from django.shortcuts import reverse
from django.utils import timezone

STATUS = (
    ('O','Ongoing'),
    ('C','Completed'),
    ('U','Upcomming')
)


class Carousal(models.Model):
    image = models.ImageField(upload_to='casrousal/', null=True)
    heading = models.CharField(max_length=15)
    description = models.CharField(max_length=100)
    link = models.URLField(max_length = 200)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Slide-{self.pk}"

class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/', null=True)    
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image-{self.pk}"

class Event(models.Model):    
    title = models.CharField(max_length=15)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='events/', null=True)
    time = models.DateField()
    status = models.CharField(default='O',choices=STATUS,max_length = 5)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"

class Blog(models.Model):    
    title = models.CharField(max_length=15)
    description = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to='blogs/', null=True)
    image2 = models.ImageField(upload_to='blogs/', null=True)
    read_time = models.IntegerField()        
    homepage_display = models.BooleanField(default=False)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"        