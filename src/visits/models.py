from django.db import models

# Create your models here.

class PageVisit(models.Model):
    path = models.TextField(null=True, blank=True)
    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, blank=True) # User who visited the page
    timestamp = models.DateTimeField(auto_now_add=True)
