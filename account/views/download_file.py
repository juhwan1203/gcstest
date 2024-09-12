from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from account.serializers import DownloadFileSerializer
from config.settings import GS_BUCKET

from account.utils import generate_signed_url

class DownloadFileAPIView(APIView):
    def post(self,request):
        serializer = DownloadFileSerializer(data = request.data)
        if not serializer.is_valid():
            return Response(
                {"message": "phone number가 존재하지 않습니다."},
                status=status.HTTP_400_BAD_REQUEST
            )
        phone_number = serializer.validated_data['phone']
        file = serializer.validated_data['file']
        bucket = GS_BUCKET
        file_path = phone_number + "/" + file
        blob = bucket.blob(file_path)
        if not blob.exists():
            return("해당 파일이 업로드 되지 않았습니다.")
        # save in server
        # save_dir = f"media/{phone_number}"
        # if not os.path.exists(save_dir):
        #     os.makedirs(save_dir)
        # blob.download_to_filename("media/"+file_path)

        signed_url = generate_signed_url(file_path=file_path)

        return Response({
            "signed_url": signed_url
        })
        
        # to Reponse only use in memory
        # with io.BytesIO() as file_stream:
        #     blob.download_to_file(file_stream)
        #     file_stream.seek(0)
        #     response = HttpResponse(
        #         file_stream.getvalue(),
        #         content_type='application/octet-stream'  # 적절한 MIME 타입 설정
        #     )
        #     response['Content-Disposition'] = f'attachment; filename="{file}"'

        # return response
        