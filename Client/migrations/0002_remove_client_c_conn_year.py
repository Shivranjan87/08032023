# Generated by Django 4.1.7 on 2023-03-07 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='c_conn_year',
        ),
    ]
