from django.db import models


class PageVisits(models.Model):
    path = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
