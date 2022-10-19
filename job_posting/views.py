from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from job_posting.serializers import JobPostingSerializer
from job_posting.models import JobPosting as JobPostingModel


# Create your views here.
class JobPostingApiView(APIView):    
    def post(self, request):
        job_posting_serializer = JobPostingSerializer(data=request.data)
        if job_posting_serializer.is_valid():
            job_posting_serializer.save()
            return Response({"message":"채용공고 등록에 성공했습니다."}, status=status.HTTP_200_OK)
        return Response(job_posting_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        job_posting = JobPostingModel.objects.get(id=request.data['post_id'])
        job_posting_serializer = JobPostingSerializer(job_posting, data=request.data, partial=True)
        if job_posting_serializer.is_valid():
            job_posting_serializer.save()
            return Response({"message":"성공적으로 채용공고를 수정하였습니다."}, status=status.HTTP_200_OK)
        return Response(job_posting_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        job_posting = JobPostingModel.objects.get(id=request.data['post_id'])
        job_posting.delete()
        return Response({"message": "성공적으로 채용공고를 삭제했습니다."}, status=status.HTTP_200_OK)
