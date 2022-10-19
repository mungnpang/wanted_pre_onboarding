from rest_framework import serializers

from job_posting.models import JobPosting as JobPostingModel
from company.models import Company as CompanyModel
from applicant.models import Apply as ApplyModel

from company.serializers import CompanySerializer


class BriefCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyModel
        fields = ["name", "country", "region"]


class PostingListSerializer(serializers.ModelSerializer):
    company = BriefCompanySerializer()
    class Meta:
        model = JobPostingModel
        fields = ["id", "company", "position", "reward", "job_skill"]


class PostingDetailSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    
    class Meta:
        model = JobPostingModel
        fields = ["id", "company", "position", "reward", "job_skill", "description"]
        

class ApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplyModel
        fields = ["post", "user"]