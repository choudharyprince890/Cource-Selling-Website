from django.db import models
from .cource import Cource
from .user_cource import UserCource 
from django.contrib.auth.models import User

class Payment(models.Model):
    order_id = models.CharField(max_length = 50, null = False)
    payment_id = models.CharField(max_length = 50)
    user_cource = models.ForeignKey(UserCource, null=True, on_delete = models.CASCADE)
    cource = models.ForeignKey(Cource, null=False, on_delete = models.CASCADE)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username