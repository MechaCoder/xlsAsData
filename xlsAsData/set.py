from os.path import isfile
from string import ascii_uppercase
from uuid import uuid1 

from openpyxl import Workbook

class Set:

    def __init__(self, filePath:str, dataHeader:str):
        self.path = filePath
        self.headers = dataHeader.split(',')

    def insert(self, data:list) -> bool:
        """ inserts data to spreadsheet """
        # if the file dose not exist create it
        # inserts all data into the sheet
        wb = Workbook()
        # adds the headers
        i = 0
        sheet = wb.active
        for header in ['uuid'] + self.headers:
            loc = ascii_uppercase[i] + str(1)
            sheet[loc] = header
            i += 1

        # adds content
        row_i = 2
        for row in data:
            if 'uuid' not in row.keys():
                row['uuid'] = str(uuid1()) # bugfix to stop the uuid changeing 


            col_i = 0

            if isinstance(row, dict) == False:
                continue

            for header in ['uuid'] + self.headers:
                loc = ascii_uppercase[col_i] + str(row_i)
                sheet[loc] = row[header]
                
                col_i += 1
            row_i += 1
            
        wb.save(self.path)
        wb.close()
