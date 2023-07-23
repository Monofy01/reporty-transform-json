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

        parsed_body_data = json.loads(record['body'])
        print(f"value record[body]: {parsed_body_data}")
        print(f"type record[body]: {type(parsed_body_data)}")
        ReportService.create_xlsx(parsed_body_data)
