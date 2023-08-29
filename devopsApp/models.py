from django.db import models

# Create your models here.
class Person(models.Model) :
    id_run = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField()
    username = models.CharField(max_length=255)
    
    class Meta:
        db_table = "persons"