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
        record_body_str = record['body']
        record_body_dict = json.loads(record_body_str)
        print(f'value record[body]: {record_body_dict}')
        print(type(record_body_dict))
        ReportService.create_xlsx(record_body_dict)
