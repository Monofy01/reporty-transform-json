import json

from src.s3.client_s3 import S3Client
from src.services.creator_xlsx import CreatorXlsx


class ReportService:
    def __int__(self):
        pass

    @staticmethod
    def create_xlsx(request_json):
        excel = json.loads(request_json['excel'])
        creator_excel = CreatorXlsx(excel)
        binary_data = creator_excel.new_xlsx()
        S3Client.upload_s3(creator_excel, binary_data)


