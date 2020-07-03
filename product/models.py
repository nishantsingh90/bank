from django.db import models

# Create your models here.ifsc,bank_id,branch,address,city,district,state,bank_name
class Bank(models.Model):
    ifsc = models.CharField(max_length=100)
    bank_id = models.CharField(max_length=100)
    branch_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=100)