from django.db import models

class Bill(models.Model):
   
    UID = models.CharField(max_length=100)
  
class Item(models.Model):
 
    UID = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=255)
    description = models.TextField()
    numberOfSplits = models.IntegerField()
    BillId = models.ForeignKey(Bill, on_delete=models.CASCADE, related_name='items')
    pricePerSplit = models.DecimalField(max_digits=10, decimal_places=2)
   
