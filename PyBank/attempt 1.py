import csv
import locale

import locale 


file_path = r'C:\Users\rockm\Python\Module-3-Python\PyBank\Resources\budget_data.csv'

# Open the CSV file
with open(file_path, 'r') as csv_file:
    reader = csv.reader(csv_file)
    
    # Read the headers from the first row
    headers = next(reader)

    # Create a set to store unique months
    unique_months = set()

    numbers = []

    numbers.ammend(row[1])

    # Initialize a variable for the total sum
    total_sum = 0

    # Iterate over each row in the CSV file
    for row in reader:
        # Extract the month from column 1
        month = row[0]
        
        # Add the month to the set of unique months
        unique_months.add(month)
        
        # Extract the value from column 2 and convert it to a float
        value = float(row[1])
        
        # Add the value to the total sum
        total_sum += value

    # Count the total number of months
    total_months = len(unique_months)
    print("Total Months:", total_months)
    
    # Print the total sum
    print("Total Sum:", total_sum)

    # Average change math
    average_change = (total_sum / total_months)

    # Display results
    print("Average Change:", average_change)