from django.db import models

class Staff(models.Model):

    id          = models.AutoField(primary_key=True)
    name        = models.CharField(max_length=50)
    email       = models.EmailField()
    department  = models.CharField(max_length=50)
    objects     = models.Manager()