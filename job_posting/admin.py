from django.contrib import admin

from job_posting.models import Skill as SkillModel
from job_posting.models import JobPosting as JobPostingModel

# Register your models here.
class Skill(admin.ModelAdmin):
    list_display = ('id', 'skill')
    
class JobPosting(admin.ModelAdmin):
    list_display = ('id', 'company', 'position', 'reward')

admin.site.register(SkillModel, Skill)
admin.site.register(JobPostingModel, JobPosting)