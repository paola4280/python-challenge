import os
import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')
#print(f"CSV Path: {csvpath}")

total_votes = 0
unique_names = []
vote_counts = {}

# Open the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader) 
    #print(f"CSV Header: {csvheader}")
    
    for row in csvreader:
        # Count total votes
        total_votes += 1
        
        # Count votes for each candidate
        candidate = row[2]
        if candidate not in vote_counts:
            vote_counts[candidate] = 0
        vote_counts[candidate] += 1
    
    print("Election Results")
    print("------------------------------")    
    # total votes and list of candidates
    print(f"Total Votes: {total_votes}")
    print("------------------------------")
   # print("Candidates list and percentage of votes:") 
    for candidate, votes in vote_counts.items():
        vote_percentage = (votes / total_votes) * 100
        print(f"{candidate}: {vote_percentage:.3f}% ({votes})")
    print("------------------------------")
    winner = max(vote_counts, key=vote_counts.get)
    print(f"Winner: {winner}")
    print("------------------------------")
    
output_path = os.path.join('..', 'Resources', 'results.txt')   
    
with open(output_path, 'w') as file:
    file.write("Election Results\n")
    file.write("------------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("------------------------------\n")
    
    for candidate, votes in vote_counts.items():
        vote_percentage = (votes / total_votes) * 100
        file.write(f"{candidate}: {vote_percentage:.3f}% ({votes})\n")
    
    file.write("------------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("------------------------------\n")
