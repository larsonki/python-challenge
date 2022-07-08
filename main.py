import os
import csv
filepath = os.path.join('Resources','budget_data.csv')
with open(filepath) as budget_data:
        csvreader=csv.reader(budget_data,delimiter=',')
        header=next(csvreader)
        print(f"{header}")
        
        