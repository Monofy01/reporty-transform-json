import json

from src.services.report_services import ReportService


def handler(event: dict, context):
    records = event['Records']
    for record in records:
        record['body'] = record['body'].replace("\\", "")[1:-1]
        body = json.loads(record['body'])
        ReportService.create_xlsx(body)
