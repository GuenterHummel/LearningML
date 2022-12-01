class CsvFileInfo:
    creation_date: str
    operator: str
    atm_identifier: str

    def __init__(self):
        self.creation_date = ''
        self.operator_name = ''
        self.atm_identifier = ''

    def __init__(self, filename: str):
        if not filename.startswith("output-"):
            return

        #filena
        self.creation_date = ''
        self.operator_name = ''
        self.atm_identifier = ''


# output-07.11.2022_PF99409999.csv
