from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from config.settings import GS_BUCKET

class UploadFileAPIView(APIView):
    def post(self, request):
        phone_number = request.POST.get('phone')
        file = request.FILES.get('file')

        if not phone_number or not file:
            return Response(
                {"message": "phone number 또는 file이 존재하지 않습니다."},
                status=status.HTTP_400_BAD_REQUEST
            )
        bucket = GS_BUCKET
        file_path = f'{phone_number}/' + file.name
        blob = bucket.blob(file_path)
        if blob.exists():
            print("try upload to file in blob, in case : blob is exist")
            blob.upload_from_file(file)
            return Response(
                {"message": "파일이 업데이트되었습니다."})
        print("try upload to file in blob")
        blob.upload_from_file(file)
        return Response(
                {"message": "파일이 업로드되었습니다."})
    