from django.db import models


# Create your models here.

class employee(models.Model):
    e_id = models.IntegerField()
    e_name = models.CharField(max_length=20)
    e_age = models.IntegerField()
    e_doj = models.DateField()
    e_role = models.CharField(max_length=5, choices=[('D', 'Developer'), ('T', 'Tester')])
    e_add = models.CharField(max_length=20)

    class Meta:
        db_table = 'Employee'
