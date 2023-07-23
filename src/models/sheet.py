import json
from typing import Tuple, Dict, List
import re


class Sheet:
    def __init__(self, name: str, columns: Tuple[str, str], data: List[dict], data_invalid: List[dict]):
        self.name = name
        self.columns = tuple(columns)
        self.data = data
        self.data_invalid = data_invalid

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)





