from rest_framework import serializers

from job_posting.models import Skill as SkillModel
from job_posting.models import JobPosting as JobPostingModel


class JobPostingSerializer(serializers.ModelSerializer):
    job_skill = serializers.ListField()
    
    class Meta:
        model = JobPostingModel
        fields = ["company", "position", "reward", "description", "job_skill"]
        
    def create(self, validated_data):
        job_skill = validated_data.pop("job_skill", [])
        recruit = JobPostingModel(**validated_data)
        recruit.save()

        for skill in job_skill:
            job_skill_object = SkillModel.objects.get(skill=skill)
            recruit.job_skill.add(job_skill_object)
            
        return recruit
    
    
    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance