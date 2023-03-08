from django.db import models


# Create your models here.

class client(models.Model):
    c_id = models.IntegerField()
    c_name = models.CharField(max_length=20)
    c_status = models.CharField(max_length=5, choices=[('A', 'Active'), ('C', 'Ceased')])
    c_add = models.CharField(max_length=20)

    class Meta:
        db_table = 'Client'
