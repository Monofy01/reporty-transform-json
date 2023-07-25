import dataclasses
import re
from typing import Dict, List, Tuple

@dataclasses.dataclass
class Sheet:
    name: str
    columns: List[Tuple]
    data: List[Dict]
    data_invalid: List[Dict] = dataclasses.field(default_factory=list)

    @classmethod
    def from_dict(cls, sheet_dict: Dict) -> 'Sheet':
        name = sheet_dict.get('name', '')
        columns = [tuple(column) for column in sheet_dict.get('columns', [])]
        data = [dict(item) for item in sheet_dict.get('data', [])]

        return cls(name, columns, data)
    def to_dict(self):
        sheet_dict = {
            "name": self.name,
            "columns": self.columns,
            "data": self.data,
            "data_invalid": self.data_invalid
        }
        return sheet_dict


