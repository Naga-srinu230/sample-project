from django.db import models

# Create your models here.
class Srinu(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age       = models.IntegerField()
    mobile_number = models.CharField(max_length=15)
    address = models.CharField(max_length=150)
    dateofbirth =models.DateField(auto_now_add=False)
    
    class Meta:
        db_table = "Srinu"
    
#srinu_instant = Srinu("Nagasrinu","v",33,"987867565","hyd",16071999)