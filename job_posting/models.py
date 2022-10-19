from django.db import models
from company.models import Company

# Create your models here.
class Skill(models.Model):
    skill = models.CharField(max_length=32)
    
    def __str__(self):
        return self.skill


class JobPosting(models.Model):
    company = models.ForeignKey(to=Company, related_name="company", on_delete=models.CASCADE)
    position = models.CharField(max_length=64)
    reward = models.IntegerField(blank=True)
    description = models.TextField()
    job_skill = models.ManyToManyField(to=Skill, related_name="job_skill")
    
    def __str__(self):
        return self.position