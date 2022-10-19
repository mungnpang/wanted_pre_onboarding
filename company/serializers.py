from rest_framework import serializers

from company.models import FundingStage as FundingStageModel
from company.models import Company as CompanyModel


class FundingStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FundingStageModel
        fields = ["funding_stage"]


class CompanySerializer(serializers.ModelSerializer):
    other_posts = serializers.SerializerMethodField()
    seed = FundingStageSerializer()
    
    def get_other_posts(self, obj):
        posts = []
        for post in obj.company.all():
            posts.append(post.id)
            
        return {"이 회사의 다른 공고들": [posts]}
    
    class Meta:
        model = CompanyModel
        fields = ["name", "country", "region", "seed", "employees", "other_posts"]