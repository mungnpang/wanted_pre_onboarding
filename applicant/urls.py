from django.urls import path
from applicant.views import PostingListApiView, SearchApiView, PostingDetailApiView, ApplyApiView

urlpatterns = [
    path('', PostingListApiView.as_view()),
    path('search/', SearchApiView.as_view()),
    path('detail/', PostingDetailApiView.as_view()),
    path('detail/apply/', ApplyApiView.as_view()),
]
