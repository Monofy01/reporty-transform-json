import json

from src.services.report_services import ReportService


def handler(event: dict, context):
    records = event['Records']
    try:
        for record in records:
            ReportService.create_xlxs(json.loads(record['body']))
    except Exception as e:
        print(e)
