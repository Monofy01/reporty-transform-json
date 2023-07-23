import json

from src.services.report_services import ReportService


def handler(event: dict, context):
    records = event['Records']
    try:
        for record in records:
            record_body_str = record['body']
            record_body_dict = json.loads(record_body_str)
            print("PRE TYPE")
            print(type(record_body_dict))
            ReportService.create_xlsx(record_body_dict)
    except Exception as e:
        print(e)