from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('students/', include('students.urls', namespace= 'students')),
    path('library/', include('library.urls', namespace='library'))
]
