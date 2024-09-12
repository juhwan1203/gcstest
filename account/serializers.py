from rest_framework import serializers

class DownloadFileSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=255)
    file =  serializers.CharField(max_length=255)

    