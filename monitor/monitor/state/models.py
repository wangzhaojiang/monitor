from django.db import models

# Create your models here.

class cpu(models.Model):
    #time = models.DateTimeField()
    ip = models.CharField(max_length = 30, default = '')
    time = models.CharField(max_length = 30)
    #user_use = models.FloatField(default = 0.0)
    #system_use = models.FloatField(default = 0.0)
    #all_use = models.FloatField(default = 0.0)
    user_use = models.CharField(max_length = 30)
    system_use = models.CharField(max_length = 30)
    all_use = models.CharField(max_length = 30)

    def __unicode__(self):
        return self.all_use


class diskio(models.Model):
    ip = models.CharField(max_length = 30, default = '')
    time = models.CharField(max_length = 30)
    #pgpgin = models.FloatField(default = 0.0)
    #pgpgout = models.FloatField(default = 0.0)
    pgpgin = models.CharField(max_length = 30)
    pgpgout = models.CharField(max_length = 30)


class flow(models.Model):
    ip = models.CharField(max_length = 30, default = '')
    time = models.CharField(max_length = 30)
    interface = models.CharField(max_length = 20)
    #byte = models.IntegerField(default = 0)
    #packets = models.IntegerField(default = 0)
    byte = models.CharField(max_length = 30)
    packets = models.CharField(max_length = 30)

class memory(models.Model):
    ip = models.CharField(max_length = 30, default = '')
    time = models.CharField(max_length = 30)
    #memuse = models.FloatField(default = 0.0)
    #memtotal = models.FloatField(default = 0.0)
    #swaptotal = models.FloatField(default = 0.0)
    #swapfree = models.FloatField(default = 0.0)
    memuse = models.CharField(max_length = 30)
    memtotal = models.CharField(max_length = 30)
    swaptotal = models.CharField(max_length = 30)
    swapfree = models.CharField(max_length = 30)

class netstat(models.Model):
    ip = models.CharField(max_length = 30, default = '')
    time = models.CharField(max_length = 30)
    types = models.CharField(max_length = 10)
    address = models.CharField(max_length = 30)
    pid_programname = models.CharField(max_length = 50)
