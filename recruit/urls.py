from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recruit/', include('job_posting.urls')),
    path('applicant/', include('applicant.urls')),
]
