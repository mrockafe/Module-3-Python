import csv

file_path = r"C:\Users\rockm\Python\Module-3-Python\PyPoll\Resources\election_data.csv"

# Open the CSV file
with open(file_path, 'r') as csv_file:
    reader = csv.reader(csv_file)
    
    # Read the headers from the first row
    headers = next(reader)

    #split columns into lists
    col1, col2, col3 = [],[], []

    for row in reader:
        col1.append(row[0])
        col2.append(row[1])
        col3.append(row[2])

    total_votes = 0

    for col1 in csv_file
        total_votes += 1

print("Election Results")
print("------------------")
print(f"Total Votes", {total_votes})