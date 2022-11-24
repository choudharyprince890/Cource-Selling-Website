from unittest.util import _MAX_LENGTH
from django.db import models
from .cource import Cource

class Videos(models.Model):
    title = models.CharField(max_length = 50, null = False)
    cource = models.ForeignKey(Cource, null=False, on_delete = models.CASCADE)
    length = models.IntegerField(null=False)
    video_id = models.CharField(max_length = 20, null = False) 
    is_preview = models.BooleanField(default = False)

    def __str__(self):
        return self.title