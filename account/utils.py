import datetime

from config.settings import GS_BUCKET

def generate_signed_url(file_path):
    bucket = GS_BUCKET
    blob = bucket.blob(file_path)
    expiration_time = datetime.timedelta(minutes=10)
    signed_url = blob.generate_signed_url(expiration = expiration_time)
    return signed_url
