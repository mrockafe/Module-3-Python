import csv

# Path to the CSV file
csv_path = r"C:\Users\rockm\Python\Module-3-Python\PyBank\Resources\budget_data.csv"

# Open the CSV file in read mode
with open(csv_path, "r") as file:
    # Establish csv as read for data
    csv_reader = csv.reader(file)

    # Skip the header row for data
    next(csv_reader)

    # Initialize variables for each result
    total_months = 0
    total_profit_loss = 0
    previous_profit_loss = 0
    changes = []
    max_increase = float('-inf')
    max_increase_month = ""
    max_decrease = float('inf')
    max_decrease_month = ""

    # Run through rows excluding headers 
    for row in csv_reader:
        # Add total months as running through rows 
        total_months += 1

        # Sum Profit/Loss in column 2, 1 in python logic 
        total_profit_loss += int(row[1])

        # Calculate the change in profit/loss through changes then ammend changes list 
        current_profit_loss = int(row[1])
        if previous_profit_loss != 0:
            change = current_profit_loss - previous_profit_loss
            changes.append(change)
            # Check if the set change is the highest increase
            if change > max_increase:
                max_increase = change
                max_increase_month = row[0]
            # Check if the set change is the greatest decrease
            if change < max_decrease:
                max_decrease = change
                max_decrease_month = row[0]
        previous_profit_loss = current_profit_loss

# Calculate the average change with total sum divide by length of list (# of changes)
average_change = sum(changes) / len(changes)

# Display the results
print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss:,}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {max_increase_month} (${max_increase:,})")
print(f"Greatest Decrease in Profits: {max_decrease_month} (${max_decrease:,})")

# Path to txt results file
output_path = r"C:\Users\rockm\Python\Module-3-Python\PyBank\analysis\PyBank_Results.txt"

# Create and write the results to txt file
with open(output_path, "w") as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${total_profit_loss:,}\n")
    output_file.write(f"Average Change: ${average_change:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {max_increase_month} (${max_increase:,})\n")
    output_file.write(f"Greatest Decrease in Profits: {max_decrease_month} (${max_decrease:,})\n")

# Display a message indicating that the file was created successfully
print("File Saved")

