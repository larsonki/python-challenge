#import file & read it
from distutils.util import change_root
import os
import csv
file_path = os.path.join('Resources','budget_data.csv')
with open(file_path) as budget_data:
        csv_reader=csv.reader(budget_data,delimiter=',')
        #read header row first
        csv_header=next(budget_data)
        #create an empty set to store # of rows for months
        total_months = set()
        #create a variable for total and set to 0
        total = 0
        change = 85
        avg_divisor = (len(total_months)-1)
        average_change = change/avg_divisor
        #read through each row of data after header
        for row in csv_reader:
                #count number of months, referencing the specific column
                #referenced code from https://stackoverflow.com/questions/
                #64857757/best-way-to-count-unique-values-from-csv-in-python
                total_months.add(row[0])
                #sum each row in the second column for the net total P/L
                total += int(row[1])
                #change = change + int(row[1]) - (int(row[1]-1))
        print("Financial Analysis")
        print("----------------------------")
        print(f"Total Months: {len(total_months)}")
        print(f"Total: ${total}")
        #print(f"Average Change: ${average_change}")
        print(avg_divisor)
        
        