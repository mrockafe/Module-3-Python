import csv

file_path = r"C:\Users\rockm\Python\Module-3-Python\PyPoll\Resources\election_data.csv"

# Open the CSV file
with open(file_path, 'r') as csv_file:
    reader = csv.reader(csv_file)
    
    # Read the headers from the first row
    headers = next(reader)

    # Initialize varables for the results
    total_votes = 0
    candidates = set()
    candidate_votes = {}
    candidate_percent = {}

    #run through rows excluding headers
    for row in reader:
        #Add total votes when running through rows
        total_votes += 1

        current_candidates = row[2]
        candidates.add(current_candidates)

        if current_candidates in candidate_votes:
            candidate_votes[current_candidates] += 1
        else:
            candidate_votes[current_candidates] = 1

        

print("Election Results")
print("------------------")
print(f"Total Votes", {total_votes})
print("------------------")
for candidate, votes in candidate_votes.items():
    percentage = round((votes / total_votes) * 100, 3)
    print(f"{candidate}: {percentage}% ({votes})")
print("------------------")

