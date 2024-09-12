from django.urls import path

from .views.upload_file import UploadFileAPIView
from .views.download_file import DownloadFileAPIView
from .views.delete_file import DeleteFileAPIView

urlpatterns = [
    path('upload', UploadFileAPIView.as_view(), name='upload_bin'),
    path('download', DownloadFileAPIView.as_view(), name='download_bin'),
    path('delete', DeleteFileAPIView.as_view(),name='delete_bin'),
]

