from django.db import models

from job_posting.models import JobPosting

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=32)
    
    def __str__(self):
        return self.username


class Apply(models.Model):
    post = models.ForeignKey(to=JobPosting, on_delete=models.CASCADE)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)