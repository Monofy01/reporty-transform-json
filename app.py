import json

from src.services.report_services import ReportService


def handler(event: dict, context):
    print(event)
    print(type(event))
    records = event['Records']

    for record in records:
        print(f"LIST + {type(records)}")
        print(f"ITEM + {type(record)}")
        print(record)

        print(f"value record[body]: {record['body']}")
        print(f"type record[body]: {type(record['body'])}")

        ReportService.create_xlsx(record['body'])
