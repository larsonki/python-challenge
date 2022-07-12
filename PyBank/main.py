# Python script to analyze Profit & Loss of a company over approx 7 years.
# import file & read it
import os
import csv
#import pandas as pd
file_path = os.path.join('Resources','budget_data.csv')
with open(file_path) as budget_data:
        csv_reader=csv.reader(budget_data,delimiter=',')
        # read header row first
        csv_header=next(budget_data)
        # create an empty set to store # of rows for months
        total_months = []
        # create a variable for total and set to 0
        total = 0
        amount = []
        change = []
        # read through each row of data after header
        for row in csv_reader:
                # count number of months, referencing the specific column
                # referenced code from James Shapiro at https://stackoverflow.com/
                # questions/64857757/best-way-to-count-unique-values-from
                # -csv-in-python
                total_months.append(row[0])
                # sum each row in the second column for the net total P/L
                total += int(row[1])
                #change = change + int(row[1]) - (int(row[1]-1))
                # create a list of all values in the P/L column & convert
                # to an integer
                amount.append(int(row[1]))
        # calculate the change between each row starting with the 2nd row minus
        # the first and looping through all values in 'amount' referenced code
        # from Jordi Fuentes at https://stackoverflow.com/questions/59494280/loop
        # -over-csv-and-subtract-previous-line-from-current-line
        for index,element in enumerate(amount[1:]): #enumerate is assigning an index to 
                # the values in the amount list so the previous rows can be referenced in the following
                # equation
                change.append(int(element)-int(amount[index])) # element0 or the 2nd amount minus 
                # element indexed at -1 or the first amount
        # calculate average change
        avg_change = sum(change)/len(change)
        max_change_index = change.index(max(change))
        min_change_index = change.index(min(change))
        max_mm_yy = total_months[max_change_index+1]
        min_mm_yy = total_months[min_change_index+1]
        print("Financial Analysis")
        print("----------------------------")
        print(f"Total Months: {len(total_months)}")
        print(f"Total: ${total}")
        print(f"Average Change: ${round(avg_change,2)}")
        print(f"Greatest Increase in Profits: {max_mm_yy} (${max(change)})")
        print(f"Greatest Decrease in Profits: {min_mm_yy} (${min(change)})")
        
        