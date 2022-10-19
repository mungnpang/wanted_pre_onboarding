from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from job_posting.models import JobPosting as JobPostingModel
from applicant.models import Apply as ApplyModel
from applicant.serializers import PostingListSerializer
from applicant.serializers import PostingDetailSerializer
from applicant.serializers import ApplySerializer


# Create your views here.
class PostingListApiView(APIView):
    def get(self, request):
        posts = JobPostingModel.objects.all()
        return Response(PostingListSerializer(posts, many=True).data, status=status.HTTP_200_OK)


class SearchApiView(APIView):
    def get(self, request):
        query = self.request.GET.get('keyword')
        posts = JobPostingModel.objects.filter(
            Q(company__name__icontains=query) |
            Q(position__icontains=query) |
            Q(job_skill__skill__icontains=query)
            ).distinct()
        return Response(PostingListSerializer(posts, many=True).data, status=status.HTTP_200_OK)


class PostingDetailApiView(APIView):
    def get(self, request):
        post = JobPostingModel.objects.get(id=request.data['id'])
        return Response(PostingDetailSerializer(post).data, status=status.HTTP_200_OK)


class ApplyApiView(APIView):
    def get(self, request):
        apply_list = ApplyModel.objects.all()
        return Response(ApplySerializer(apply_list, many=True).data, status=status.HTTP_200_OK)
    
    def post(self, request):
        apply_serializer = ApplySerializer(data=request.data)
        if apply_serializer.is_valid():
            apply_serializer.save()
            return Response({"message":"지원 완료!"}, status=status.HTTP_200_OK)
        return Response(apply_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


