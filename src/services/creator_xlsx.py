import json

from openpyxl.workbook import Workbook

from src.models.excel import Excel


class CreatorXlsx:
    def __init__(self, data_xlsx):
        self.workbook = Workbook()
        self.excel_raw = data_xlsx
        self.log_output = []
        self.excel = Excel(data_xlsx['filename'], data_xlsx['webhook'], data_xlsx['sheets'])


    def new_xlsx(self):
        for sheet_file in self.excel.sheets:
            sheet = self.workbook.create_sheet(title=sheet_file.name)

            for column_index, column_name in enumerate(sheet_file.columns, start=1):
                sheet.cell(row=1, column=column_index, value=column_name[0])

            for row_index, row_data in enumerate(sheet_file.data, start=2):
                for column_index, column_name in enumerate(sheet_file.columns, start=1):
                    cell_value = row_data.get(column_name[0])
                    sheet.cell(row=row_index, column=column_index, value=cell_value)
            if len(sheet_file.data_invalid) > 0:
                self.log_output.append([dict(sheet_file.columns), *sheet_file.data_invalid])

        self.workbook.remove(self.workbook.active)
        self.workbook.save(f'/tmp/{self.excel.filename}.xlsx')

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
