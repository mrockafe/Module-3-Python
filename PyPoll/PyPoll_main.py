import csv

file_path = r"F:\Module-3-Python\PyPoll\Resources\election_data.csv"

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
print(f"Total Votes", total_votes)
print("------------------")
for candidate, votes in candidate_votes.items():
    percentage = round((votes / total_votes) * 100, 3)
    print(f"{candidate}: {percentage}% ({votes})")
print("------------------")
winner = max(candidate_votes, key=candidate_votes.get)
print(f"Winner: {winner}")

# Path to txt results file
output_path = r'F:\Module-3-Python\PyPoll\analysis\election_results.txt'

# Create and write the results to txt file
with open(output_path, "w") as output_file:
    output_file.write("Election Results\n")
    output_file.write("------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("------------------\n")
    for candidate, votes in candidate_votes.items():
            percentage = round((votes / total_votes) * 100, 3)   
    output_file.write(f"{candidates}: {percentage}% ({votes})\n")
    output_file.write("------------------\n")
    output_file.write(f"Winner: {winner}\n") 

# Display a message indicating that the file was created successfully
print("File Saved")