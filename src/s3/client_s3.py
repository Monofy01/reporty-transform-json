import io
import json
import zipfile
from io import BytesIO

import boto3

from src.config.enviroments import ENVS


class S3Client:
    def __init__(self):
        self.data = ""

    @staticmethod
    def create_zip_buffer(creator_excel, binary_data_xlsx, binary_data_log):
        try:
            print("Creating ZIP buffer")
            zip_buffer = io.BytesIO()
            with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
                zip_file.writestr(f"{creator_excel.excel.filename}.xlsx", binary_data_xlsx)
                zip_file.writestr(f"{creator_excel.excel.filename}-logs.txt", binary_data_log)

            zip_buffer.seek(0)
            binary_zip = zip_buffer.getvalue()
            zip_buffer.close()
            print("ZIP buffer created")
            return binary_zip
        except Exception as e:
            print("Error creating ZIP buffer:", e)

    @staticmethod
    def upload_zip_to_s3(creator_excel, binary_data_xlsx, binary_data_log):
        try:
            zip_buffer = S3Client.create_zip_buffer(creator_excel, binary_data_xlsx, binary_data_log)
            print("Uploading ZIP file to S3")
            s3 = boto3.client('s3')

            zip_bytesio = io.BytesIO(zip_buffer)
            s3.upload_fileobj(zip_bytesio, ENVS.S3_BUCKET_NAME, f"{creator_excel.excel.filename}/{creator_excel.excel.filename}.zip")

            print("ZIP file uploaded to S3")
            return True
        except Exception as e:
            print("Error uploading ZIP file to S3:", e)


    @staticmethod
    def upload_s3(creator_excel, binary_data):
        try:
            bynary_xlsx = S3Client.upload_xlsx_to_s3(creator_excel, binary_data)
            bynary_logs = S3Client.upload_logs_to_s3(creator_excel)
            S3Client.upload_json_to_s3(creator_excel)
            S3Client.upload_zip_to_s3(creator_excel, bynary_xlsx, bynary_logs)
        except Exception as e:
            print("Error uploading file to S3:", e)

    @staticmethod
    def upload_xlsx_to_s3(creator_excel, binary_data):
        try:
            print("Realizando carga de archivo XLSX")
            s3 = boto3.client('s3')
            buffer = io.BytesIO(binary_data)
            buffer.seek(0)
            binary_xlsx = buffer.getvalue()
            s3.upload_fileobj(buffer, ENVS.S3_BUCKET_NAME,
                              f"{creator_excel.excel.filename}/{creator_excel.excel.filename}.xlsx")
            buffer.close()
            print("Carga exitosa de archivo XLSX")
            return binary_xlsx
        except Exception as e:
            print("Error uploading XLSX file to S3:", e)
            return None


    @staticmethod
    def upload_logs_to_s3(creator_excel):
        s3 = boto3.client('s3')
        try:
            if len(creator_excel.log_output) > 0:
                print("Realizando carga de archivo LOGS")
                text = str(creator_excel.log_output).replace("'", "\"")
                buffer = io.BytesIO(text.encode())
                buffer.seek(0)
                binary_logs = buffer.getvalue()
                s3.upload_fileobj(buffer, ENVS.S3_BUCKET_NAME, f'{creator_excel.excel.filename}/{creator_excel.excel.filename}-logs.txt')
                buffer.close()
                print("Carga de archivo LOGS exitosa")
                return binary_logs
        except Exception as e:
            print("Error uploading LOGS file to S3:", e)
            return None

    @staticmethod
    def upload_json_to_s3(creator_excel):
        s3 = boto3.client('s3')
        try:
            print("Realizando carga de archivo JSON")
            json_string = json.dumps(creator_excel.excel_raw)
            buffer = io.BytesIO(json_string.encode())
            buffer.seek(0)
            s3.upload_fileobj(buffer, ENVS.S3_BUCKET_NAME,f'{creator_excel.excel.filename}/{creator_excel.excel.filename}.json')
            buffer.close()
            print("Carga exitosa de archivo JSON")
            return True
        except Exception as e:
            print("Error uploading JSON file to S3:", e)
            return None

