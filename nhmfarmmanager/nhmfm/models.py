from django.db import models

class NHMHost(models.Model):
    name = models.CharField(max_length=200)
    ip = models.CharField(max_length=13)
    api = models.CharField(max_length=10)

    def __str__(self):              # __unicode__ on Python 2
        return self.name
    

