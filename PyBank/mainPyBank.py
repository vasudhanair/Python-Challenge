# First we'll import the os module
import os
# Module for reading CSV files
import csv

# Set path for file
csvpath = os.path.join("..", "Resources", 'budget_data.csv')

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    next(csvreader)

    # The total number of months included in the dataset
    Total_months = sum(1 for row in csvreader)
    print("Total months :" + str(Total_months))

    Total_months = 0
    columnvalue = 0
    for row in csvreader:
        Total_months += 1
        columnvalue = float(row[1]) + columnvalue

        listcolumnvalue = []
        listcolumnvalue.append(columnvalue)
        minvalue = min(listcolumnvalue)
    average = columnvalue / Total_months
    print("Total:" + str(columnvalue))
    print("Average Change:" + str(average))
    print("Greatest Decrease in Profits:" + str(minvalue))


    average = columnvalue/ Total_months

    listcolumnvalue = []
    for columnvalue in csvreader:
        listcolumnvalue.insert(columnvalue)
        minvalue = min(listcolumnvalue)
        maxvalue = max(listcolumnvalue)
    print("Greatest Increase in Profits:" + str(maxvalue))
    print("Greatest Decrease in Profits:" + str(minvalue))



















