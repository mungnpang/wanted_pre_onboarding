from django.urls import path
from job_posting.views import JobPostingApiView

urlpatterns = [
    path('posts', JobPostingApiView.as_view()),
]
