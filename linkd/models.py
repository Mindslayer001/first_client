from django.db import models

class LinkData(models.Model):
    zoomlink = models.URLField(max_length=200)
    def __str__(self):
        return "zoomlink"