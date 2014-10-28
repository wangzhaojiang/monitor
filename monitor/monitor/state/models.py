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
    pgpgin = models.FloatField(default = 0.0)
    pgpgout = models.FloatField(default = 0.0)


class flow(models.Model):
    time = models.CharField(max_length = 30)
    interface = models.CharField(max_length = 20)
    byte = models.IntegerField(default = 0)
    packets = models.IntegerField(default = 0)

class memory(models.Model):
    time = models.CharField(max_length = 30)
    memuse = models.FloatField(default = 0.0)
    memtotal = models.FloatField(default = 0.0)
    swaptotal = models.FloatField(default = 0.0)
    swapfree = models.FloatField(default = 0.0)

class netstat(models.Model):
    time = models.CharField(max_length = 30)
    types = models.CharField(max_length = 10)
    address = models.CharField(max_length = 30)
    pid_programname = models.CharField()
