# First we'll import the os module
import os
# Module for reading CSV files
import csv

csvpath = os.path.join("..", "Resources", 'budget_data.csv')

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
























