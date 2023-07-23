import json

from src.services.report_services import ReportService


def handler(event, context):
    print(event)
    records = event['Records']

    for record in records:
        body = record['body']
        excel_json = json.loads(body)
        ReportService.create_xlxs(excel_json)
