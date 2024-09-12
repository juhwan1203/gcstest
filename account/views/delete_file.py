from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from config.settings import GS_BUCKET
from account.serializers import DownloadFileSerializer

class DeleteFileAPIView(APIView):
    def delete(self, request):
        serializer = DownloadFileSerializer(data = request.data)
        if not serializer.is_valid():
            return Response(
                {"message": "phone number가 존재하지 않습니다."},
                status=status.HTTP_400_BAD_REQUEST
            )
        phone_number = serializer.validated_data['phone']
        file = serializer.validated_data['file']
        bucket = GS_BUCKET
        file_path = f'{phone_number}/' + file
        blob = bucket.blob(file_path)
        if blob.exists():
            try:
                blob.delete()
                return Response(
                {"message": "파일이 삭제되었습니다."})
            except Exception as e:
                return Response(
                {"error": f"애러 발생 : {e}"})

    