from uuid import uuid1

from .get import Get
from .set import Set

class XlsAsData:

    def __init__(self, file:str, tableHeaders:str) -> None:
        self.path = file
        self.headers = tableHeaders

    def create(self, newRow:dict = {}) -> bool:
        """ adds a row to the xls file """

        getObj = Get(self.path)
        
        try: 
            data = getObj.read()
        except FileNotFoundError:
            data = []

        data.append(newRow)

        setObj = Set(self.path, self.headers)
        setObj.insert(data=data)

        return True

    def read(self) -> list:
        """ reurns all rows as a list dict """
        getObj = Get(self.path)
        try: 
            return getObj.read()
        except FileNotFoundError:
            return []

    def update(self, uuid:str, newRow:dict) -> bool:
        """ updates a row based on the uuid"""
        
        data = newRow
        data['uuid'] = uuid1

        rows = []
        for e in self.read():
            if e['uuid'] == uuid1:
                e = data
            rows.append(e)
        
        setObj = Set(self.path, self.headers)
        setObj.insert(data=rows)
        return True

    def delete(self, uuid:str) -> bool:
        """removes a row form the file"""

        rows = []
        for row in self.read():
            if row['uuid'] != uuid:
                rows.append(row)
        
        setObj = Set(self.path, self.headers)
        setObj.insert(data=rows)
        return True
