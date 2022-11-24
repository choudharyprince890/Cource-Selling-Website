from django.db import models
from .cource import Cource
from django.contrib.auth.models import User

class UserCource(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    cource = models.ForeignKey(Cource, null=False, on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.cource.name}'