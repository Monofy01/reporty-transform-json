import json

from src.services.report_services import ReportService


def handler(event, context):
    print(event)
    records = event['Records']

    for record in records:
        ReportService.create_xlxs(record['body'])
