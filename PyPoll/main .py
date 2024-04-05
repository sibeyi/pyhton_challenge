import os
import csv
from collections import Counter

# Define PyPoll's variables
VotersCandidates = []

# Change directory to the directory of current python script
os.chdir(os.path.dirname(__file__))

# Path to collect data from the Resources folder
election_data_csv_path = os.path.join("Resources", "election_data.csv")

# Open and read csv
with open(election_data_csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    # Read the header row first
    csv_header = next(csvfile)
    # Read through each row of data after the header
    for row in csv_reader:
        VotersCandidates.append(row[2])

# Count votes per candidate
CandidateCounter = Counter(VotersCandidates)

# Calculate total votes
TotalVotes = sum(CandidateCounter.values())

# Calculate the percentage of votes per candidate and determine the winner
Winner = None
MaximumVotes = 0
Results = []
for Candidate, Votes in CandidateCounter.items():
    Percentage = (Votes / TotalVotes) * 100
    Results.append((Candidate, Votes, Percentage))
    if Votes > MaximumVotes:
        Winner = Candidate
        MaximumVotes = Votes

# -->>  Print the analysis to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes:  {TotalVotes}")
print("-------------------------")
for Candidate, Votes, Percentage in Results:
    print(f"{Candidate}: {Percentage:.3f}% ({Votes})")
print("-------------------------")
print(f"Winner:  {Winner}")
print("-------------------------")

# -->>  Export a text file with the results
election_file = os.path.join("Output", "election_data.txt")
with open(election_file, "w") as outfile:
    outfile.write("Election Results\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Total Votes:  {TotalVotes}\n")
    outfile.write("-------------------------\n")
    for Candidate, Votes, Percentage in Results:
        outfile.write(f"{Candidate}: {Percentage:.3f}% ({Votes})\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Winner:  {Winner}\n")
    outfile.write("-------------------------\n")