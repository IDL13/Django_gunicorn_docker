import csv

from typing import *


class Csv:   
    def __len__(self) -> int:
        return len(self.read_csv()) - 1 if len(self.read_csv()) != 0 else len(self.read_csv())
    
    @staticmethod
    def read_csv(filename:object):
        csv_array = []
        inv_numb_set = set()
        
        with filename.file.open(mode="r") as f:
            csv_reader = csv.reader(f, delimiter = ";") 

            for row in csv_reader:
                # if row[2] != "" and row[2] not in inv_numb_set:   
                #     inv_numb_set.add(row[2])
                #     csv_array.append(row)
                # elif row[2] != "":
                #     row[2] = row[2] + "(пов)"
                #     csv_array.append(row)
                # else:
                #     row[2] = "пусто"
                #     csv_array.append(row)
                csv_array.append(row)
            
            # for row in csv_reader:
            #     csv_array.append(row)
                
        return csv_array
    
    @staticmethod
    def write_in_csv(dataSet:List[str], path:str):
        try:
            with open(path, "w", newline="\n", encoding="cp1251") as f:
                writer = csv.writer(f, delimiter=";")
                writer.writerow(["Основное средство", "Гр. уч", "Инвентарный номер","Серийный номер" "ЦМО", "Дата ввода в эксплуатацию", "Дата принятия к учету", "Количество"])
                
                for row in dataSet:
                    writer.writerow(row) 

            return 0
        except:
            return 1
    
    