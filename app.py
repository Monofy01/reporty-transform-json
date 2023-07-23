import json

from src.services.report_services import ReportService


def handler(event: dict, context):
    print(f'REQUEST :: {event}')
    try:
        records = event['Records']
        for record in records:
            record['body'] = record['body'].replace("\\", "")[1:-1]
            body = json.loads(record['body'])
            ReportService.create_xlsx(body)

        return {
            'statusCode': 200,
            'body': "El archivo se ha CARGADO correctamente a procesar"
        }
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': str(e)
        }
