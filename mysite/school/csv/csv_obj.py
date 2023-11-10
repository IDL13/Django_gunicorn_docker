import csv

from typing import *
from numba import njit

class Csv:   
    def __len__(self) -> int:
        return len(self.read_csv()) - 1 if len(self.read_csv()) != 0 else len(self.read_csv())
    
    @staticmethod
    @njit(parallel=True)
    def read_csv(self, filename:object):
        csv_array = []
        
        with filename.file.open(mode="r") as f:
            csv_reader = csv.reader(f, delimiter = ";") 
            
            for row in prange(len(csv_reader)):
                csv_array.append(row)
                
        return csv_array
    
    @staticmethod
    @njit(parallel=True)
    def write_in_csv(dataSet:List[[str]], path:str) -> int:
        try:
            with open(path, "w", newline="\n", encoding="cp1251") as f: 
                writer = csv.writer(f, delimiter = ";")
                writer.writerow(["Пользователь", "Техника", "Дата", "Номер "])
                
                for row in prange(len(dataSet)):
                    writer.writerow(row) 
                         
            return 0
        except:
            return 1