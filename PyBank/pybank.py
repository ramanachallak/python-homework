# import pathlib and csv library

from pathlib import Path
import csv

# read csv file path

budget_csvpath = Path('Resources/budget_data.csv')


# declare variables

'''
month_count variable holds the count of the number of months
total_profit variable holds the Sum of all the profits
profit_difference is a variable that stores the change in profit between months, to calculate the maximum increase and decrease in profits
average_change_profit is a variable to store the average change in profits during the overall period captured in the csv, calculated as total_change_profit/difference_count
total_change_profit is a variable to store the total change in profits from the csv
difference_count is a variable to store the number of rows resulting in calculating the difference in month to month profits
greatest_increase_profits is a variable to store the greatest increase in profits for a given 2 month period in the csv
greatest_decrease_profts is a variable to store the greatest decrease in profits for a given 2 month period in the csv
greatest_increase_month is the variable to store the month in which the greatest profit increase was observed
greatest_decrease_month is the variable to store the month in which the greatest profit decrease was observed

profit_list is a list that holds the rows from the budget_csv file

'''

month_count = 0
total_profit = 0
profit_difference = 0
average_change_profit = 0
total_change_profit = 0
difference_count = 0
greatest_increase_profits = 0
greatest_decrease_profits = 0
greatest_increase_month = ""
greatest_decrease_month = ""

# list to extract the csv rows

profit_list = []


# function definition

'''
The calculate_profit_difference function takes in 2 arguments, the first being the profit observed during month n, while the second argument is the profit observed during month n+1

The function typecasts the profits from strings to integer, calculates the difference between the profits and returns the same
'''

def calculate_profit_difference(profit_month1, profit_month2):

    return int(profit_month2)-int(profit_month1)


# read and write content of budget file to a list

with open(budget_csvpath, 'r') as budget_csvfile:

    budget_csvreader = csv.reader(budget_csvfile, delimiter=',')
    budget_header = next(budget_csvreader)

    for budget_row in budget_csvreader:
        profit_list.append(budget_row)
        month_count +=1
        total_profit += int(budget_row[1])


    
for list_index in range(len(profit_list)-1):
    
    profit_difference = calculate_profit_difference(profit_list[list_index][1], profit_list[list_index+1][1])
    
    total_change_profit = total_change_profit + profit_difference
    difference_count = difference_count + 1

    if profit_difference>greatest_increase_profits:
        greatest_increase_profits = profit_difference
        greatest_increase_month = profit_list[list_index+1][0]
    elif profit_difference < greatest_decrease_profits:
        greatest_decrease_profits = profit_difference
        greatest_decrease_month = profit_list[list_index+1][0]


average_change_profit = round(total_change_profit/difference_count, 2)


# Statements to print analysis to terminal

print("Financial Analysis")
print("----------------------------")
print(f"Total months {month_count}")
print(f"Total ${total_profit}")
print(f"  Average Change: ${average_change_profit}")

print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_profits})")

print(f"  Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_profits})")


# create output file
output_path = 'output.txt'


# write to output file

with open(output_path, 'w') as file:
    # Write the above statements to the output file
        
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total months {month_count}\n")
    file.write(f"Total ${total_profit}\n")
    file.write(f"  Average Change: ${average_change_profit}\n")

    file.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_profits})\n")

    file.write(f"  Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_profits})\n")