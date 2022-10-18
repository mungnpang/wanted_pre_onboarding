from django.contrib import admin

from company.models import FundingStage as FundingStageModel
from company.models import Company as CompanyModel

# Register your models here.
class FundingStage(admin.ModelAdmin):
    list_display = ('id', 'funding_stage')
    
class Company(admin.ModelAdmin):
    list_display = ('id', 'name')
    
admin.site.register(FundingStageModel, FundingStage)
admin.site.register(CompanyModel, Company)