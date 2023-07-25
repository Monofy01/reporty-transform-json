import dataclasses
from typing import List

from src.models.sheet import Sheet


@dataclasses.dataclass
class Excel:
    filename: str
    webhook: str
    sheets: List[Sheet]
    log_output: list = dataclasses.field(default_factory=list)

    def to_dict(self):
        excel_dict = {
            "filename": self.filename,
            "webhook": self.webhook,
            "sheets": [sheet.__dict__ for sheet in self.sheets],
            "log_output": self.log_output
        }
        return excel_dict


    def __post_init__(self):
        for s in self.sheets:
            self.log_output.append([s.columns, s.data_invalid])



