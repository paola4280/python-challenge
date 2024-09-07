import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
print(f"CSV Path: {csvpath}")

csvheader = []
total_months = 0
PnLTotal = 0
prev_PnL = None  
changes = []     
dates = []       
greatest_increase = 0
greatest_increase_date = ''
greatest_decrease = 0
greatest_decrease_date = ''

# Open the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    print(f"CSV Header: {csvheader}")
    
    for row in csvreader:
        # Total number of months
        total_months += 1
        
        # Net P&L calculations
        current_PnL = int(row[1])
        PnLTotal += current_PnL  
        
        # P&L Change calculations
        if prev_PnL is not None:
            change = current_PnL - prev_PnL
            changes.append(change)
            dates.append(row[0])  # Track the date corresponding to the change
            
            # Check for greatest increase
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_date = row[0]
                
            # Check for greatest decrease
            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_date = row[0]
            
            
        # Update the previous PnL to the current one
        prev_PnL = current_PnL

    # Calculate average
    if changes:  
        avg_change = sum(changes) / len(changes)
    else:
        avg_change = 0

    # Print Statements
    print("Financial Analysis")
    print("-----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${PnLTotal}")
    print(f"Average Change: ${avg_change:.2f}") #float with 2 decimals
    print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")
    
#Write to a .txt file
output_path = os.path.join('..', 'Resources', 'results.txt')

# Open the file in write mode
with open(output_path, 'w') as file:
    # Write the financial analysis results
    file.write("Financial Analysis\n")
    file.write("-----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${PnLTotal}\n")
    file.write(f"Average Change: ${avg_change:.2f}\n")  # float with 2 decimals
    file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")

