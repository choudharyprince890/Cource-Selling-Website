from django.db import models

class Cource(models.Model):
    name = models.CharField(max_length = 50, null = False)
    slug = models.CharField(max_length = 50, null = False, unique = True)
    desc = models.TextField(max_length=500, null=True)
    prince = models.IntegerField(null=False)
    discount = models.IntegerField(null=False, default=0)
    active = models.BooleanField(default = False)
    thumbnail = models.ImageField(upload_to='files/thumbnail')
    date = models.DateTimeField(auto_now_add = True)
    resource = models.FileField(upload_to='files/resources')
    length = models.IntegerField(null=False)

    def __str__(self):
        return self.name

class Hashtag(models.Model):
    tag = models.CharField(max_length=20, null =False)
    cource = models.ForeignKey(Cource, null=False, on_delete = models.CASCADE)


class Prerequisite(models.Model):
    required = models.CharField(max_length=20, null =False)
    cource = models.ForeignKey(Cource, null=False, on_delete = models.CASCADE)

class Learning(models.Model):
    tech_learn = models.CharField(max_length=20, null =False)
    cource = models.ForeignKey(Cource, null=False, on_delete = models.CASCADE)
