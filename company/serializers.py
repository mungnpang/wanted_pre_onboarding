from rest_framework import serializers

from company.models import FundingStage as FundingStageModel
from company.models import Company as CompanyModel


class FundingStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FundingStageModel
        fields = ["funding_stage"]
        

class CompanySerializer(serializers.ModelSerializer):
    seed = FundingStageSerializer()
    class Meta:
        model = CompanyModel
        fields = ["name", "country", "region", "seed", "employees"]
        