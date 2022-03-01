# -*- coding: UTF-8 -*-
"""PyRamen Homework Starter."""

# @TODO: Import libraries
import csv
from pathlib import Path

# @TODO: Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path('Resources/menu_data.csv')
sales_filepath = Path('Resources/sales_data.csv')

# @TODO: Initialize list objects to hold our menu and sales data
menu_csv = []
sales_csv = []

# function to return list from csv file

def return_csv_list(csvpath):

    list = []

    with open(csvpath, 'r') as csvfile:

        csvreader = csv.reader(csvfile, delimiter=',')
        header = next(csvreader)

        for row in csvreader:
            list.append(row)
            
    return list  

# @TODO: Read in the menu data into the menu list

menu_csv = return_csv_list(menu_filepath)

# @TODO: Read in the sales data into the sales list

sales_csv = return_csv_list(sales_filepath)



# @TODO: Initialize dict object to hold our key-value pairs of items and metrics
report = {}

# Initialize a row counter variable
row_count = 0

# @TODO: Loop over every row in the sales list object


    

# for sales_row in sales_csv:

for sales_row in sales_csv:
    


    # Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item
    # @TODO: Initialize sales data variables

    # Line_Item_ID = sales_row[0]
    # Date = sales_row[1]
    # Credit_Card_Number = sales_row[2]
    # Quantity = sales_row[3]
    # Menu_Item = sales_row[4]
    
    Line_Item_ID = sales_row[0]
    Date = sales_row[1]
    Credit_Card_Number = sales_row[2]
    Quantity = sales_row[3]
    Menu_Item = sales_row[4]


    # @TODO:
    # If the item value not in the report, add it as a new entry with initialized metrics
    # Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit

    if Menu_Item not in report:
        report[Menu_Item] = {"01-count": 0, "02-revenue": 0, "03-cogs": 0, "04-profit": 0}
        
        for menu_row in menu_csv:
        
            Item = menu_row[0]
            Description = menu_row[2]
            Price = menu_row[3]
            Cost = menu_row[4]
            
            int_price = float(Price)
            int_quantity = int(Quantity)
            int_cost = float(Cost)
        
            profit = int_price - int_cost


        
            if Item == Menu_Item:

                report[Menu_Item]["01-count"] += int_quantity
                report[Menu_Item]["02-revenue"] += int_price * int_quantity
                report[Menu_Item]["03-cogs"] += int_cost * int_quantity
                report[Menu_Item]["04-profit"] += profit * int_quantity
        
        
    else: 


    # @TODO: For every row in our sales data, loop over the menu records to determine a match

        for menu_row in menu_csv:
            
            
        # Item,Category,Description,Price,Cost
        # @TODO: Initialize menu data variables

            Item = menu_row[0]
            Description = menu_row[2]
            Price = menu_row[3]
            Cost = menu_row[4]
            
            
            


        # @TODO: Calculate profit of each item in the menu data
        
            int_price = float(Price)
            int_quantity = int(Quantity)
            int_cost = float(Cost)
        
            profit = int_price - int_cost


        # @TODO: If the item value in our sales data is equal to the any of the items in the menu, then begin tracking metrics for that item
            if Item == Menu_Item:

                report[Menu_Item]["01-count"] += int_quantity
                report[Menu_Item]["02-revenue"] += int_price * int_quantity
                report[Menu_Item]["03-cogs"] += int_cost * int_quantity
                report[Menu_Item]["04-profit"] += profit * int_quantity

            # @TODO: Print out matching menu data
            
                


            # @TODO: Cumulatively add up the metrics for each item key
            
            
            





        # @TODO: Else, the sales item does not equal any fo the item in the menu data, therefore no match



    # @TODO: Increment the row counter by 1
    
    row_count += 1


# @TODO: Print total number of records in sales data

print(f"total sales data {row_count}")




# @TODO: Write out report to a text file (won't appear on the command line output)

output_path = 'output.txt'


# write to output file

with open(output_path, 'w') as file:
    
    file.write(f"total sales data {row_count}\n")
    file.write({report})
    