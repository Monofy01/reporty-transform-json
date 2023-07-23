import json
from typing import List

from src.models.sheet import Sheet


class Excel():
    SCHEMA_NAME = 'reports'

    def __init__(self, filename: str, webhook: bool, sheets: List[Sheet]):
        self.filename = filename
        self.webhook = webhook
        self.sheets = self.create_sheets(sheets)


    def create_sheets(self, sheets):
        return [Sheet(item['name'], item['columns'], item['data'], item['data_invalid']) for item in sheets]

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)






