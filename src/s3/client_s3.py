import io
import json
from io import BytesIO

import boto3

from src.config.enviroments import ENVS


class S3Client:
    def __init__(self):
        self.data = ""

    @staticmethod
    def upload_s3(creator_excel, binary_data):
        try:
            S3Client.upload_xlsx_to_s3(creator_excel, binary_data)
            S3Client.upload_logs_to_s3(creator_excel)
            S3Client.upload_json_to_s3(creator_excel)
        except Exception as e:
            print("Error uploading file to S3:", e)

    @staticmethod
    def upload_xlsx_to_s3(creator_excel, binary_data):
        try:
            print("Realizando carga de archivo XLSX")
            s3 = boto3.client('s3')
            buffer = io.BytesIO(binary_data)
            buffer.seek(0)
            s3.upload_fileobj(buffer, ENVS.S3_BUCKET_NAME,
                              f"{creator_excel.excel.filename}/{creator_excel.excel.filename}.xlsx")
            buffer.close()
            print("Carga exitosa de archivo XLSX")
        except Exception as e:
            print("Error uploading XLSX file to S3:", e)



    @staticmethod
    def upload_logs_to_s3(creator_excel):
        s3 = boto3.client('s3')
        try:
            if len(creator_excel.log_output) > 0:
                print("Realizando carga de archivo LOGS")
                text = str(creator_excel.log_output).replace("'","\"")

                with BytesIO() as file_obj:
                    file_obj.write(text.encode())  # Escribir el texto en el archivo en memoria
                    file_obj.seek(0)  # Reiniciar la posición del cursor al principio del archivo en memoria

                    s3.upload_fileobj(file_obj, ENVS.S3_BUCKET_NAME, f'{creator_excel.excel.filename}/{creator_excel.excel.filename}-logs.txt')  # Subir el archivo al bucket de S3
                    # TODO: REVISAR MEMORY LEAKS
                print("Carga de archivo LOGS exitosa")
                return True
        except Exception as e:
            print("Error uploading LOGS file to S3:", e)

    @staticmethod
    def upload_json_to_s3(creator_excel):
        s3 = boto3.client('s3')
        try:
            json_string = json.dumps(creator_excel.excel_raw)

            # Create a BytesIO object and write the JSON string to it
            with BytesIO() as file_obj:
                file_obj.write(json_string.encode())
                file_obj.seek(0)

                # Upload the file object to S3
                s3.upload_fileobj(file_obj, ENVS.S3_BUCKET_NAME, f'{creator_excel.excel.filename}/{creator_excel.excel.filename}.json')
        except Exception as e:
            print("Error uploading JSON file to S3:", e)

