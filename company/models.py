from django.db import models

# Create your models here.
class FundingStage(models.Model):
    funding_stage = models.CharField(max_length=16)
    
    def __str__(self):
        return self.funding_stage

class Company(models.Model):
    name = models.CharField(max_length=64, unique=True, null=False, blank=False)
    country = models.CharField(max_length=32)
    region = models.CharField(max_length=32, null=False, blank=False)
    seed = models.ForeignKey(to=FundingStage, related_name="company_seed", on_delete=models.CASCADE)
    employees = models.IntegerField()
    
    def __str__(self):
        return self.name