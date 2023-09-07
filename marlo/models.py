from django.db import models

# Create your models here.
class Product(models.Model):
    name= models.CharField(max_length=255, blank=False, null=False)
    barcode= models.IntegerField( blank=False, null=False)
    brand= models.CharField(max_length=255, blank=False, null=False)
    description= models.CharField(max_length=255, blank=False, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2 , null=False)
    available= models.CharField(max_length=25, blank=False, null=False)

    def __str__(self):
        return self.name

    
