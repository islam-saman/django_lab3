from django.db import models

class Student(models.Model):
    id          = models.AutoField(primary_key=True)
    name        = models.CharField(max_length=50)
    email       = models.EmailField()
    track       = models.CharField(max_length=50)
    password    = models.CharField(max_length=50)
    staffObj    = models.ForeignKey(to='staff.Staff',on_delete=models.CASCADE)

