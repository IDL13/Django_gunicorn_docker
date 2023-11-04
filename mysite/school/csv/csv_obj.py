import csv
from typing import *

class Csv:
    def __init__(self, filename = None):
        ...
        
    def __len__(self) -> int:
        return len(self.read_csv()) - 1 if len(self.read_csv()) != 0 else len(self.read_csv())
        
    def read_csv(self, filename:object):
        csv_array = []
        
        with filename.file.open(mode="r") as f:
            csv_reader = csv.reader(f, delimiter = ";") 
            
            for row in csv_reader:
                csv_array.append(row)
                
        return csv_array
    
    def write_in_csv(self, dataSet:List[[str]], path:str) -> int:
        try:
            with open(path, "w", newline="\n", encoding="cp1251") as f: 
                writer = csv.writer(f, delimiter = ";")
                writer.writerow(["Пользователь", "Техника", "Дата", "Номер "])
                for row in dataSet:
                    writer.writerow(row)
                    
            return 0
        
        except:
            return 1