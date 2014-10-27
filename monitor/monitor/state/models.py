from django.db import models

# Create your models here.

class cpu(models.Model):
    #time = models.DateTimeField()
    time = models.CharField(max_length = 30)
    user_use = models.FloatField(default = 0.0)
    system_use = models.FloatField(default = 0.0)
    all_use = models.FloatField(default = 0.0)

    def __unicode__(self):
        return self.all_use


class diskio(models.Model):
    time = models.CharField(max_length = 30)
    pgpgin = models.FloatField(default = 0)
    pgpgout = models.FloatField(default = 0)


class 
