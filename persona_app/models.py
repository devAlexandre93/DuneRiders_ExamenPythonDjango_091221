from django.db import models

# Create your models here.

class Persona(models.Model):
    
    password = models.CharField(max_length=20)    
    picture = models.CharField(max_length=60)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address_street = models.CharField(max_length=50)
    adress_number = models.IntegerField()
    city = models.CharField(max_length=15)
    country = models.CharField(max_length=15)
    postcode = models.IntegerField()
    email = models.EmailField(max_length=40)
    age = models.IntegerField()
    username = models.CharField(max_length=20)
    
    
    def __str__(self):
        return(f"({self.id}) {self.first_name} {self.last_name}")