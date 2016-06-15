# -- coding: utf8 --
from django.db import models

class User(models.Model):
    uname = models.CharField()
    passwd = models.CharField()
    regtime = models.DateTimeField()
    rank = models.IntegerField()
    class Meta:
        db_table = 'user'
