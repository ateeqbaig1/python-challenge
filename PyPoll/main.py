# Importing dependencies
import os
import csv
import collections
from collections import Counter

# Setting directories
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
# Input file path
InputFilePath = os.path.join("Resources", "election_data.csv")
# Output file path
OutputFilePath = os.path.join("Results", "PyPoll.txt")

# Variables
Candidates = []
VotesPerCandidate = []

# Opening and reading file
with open(InputFilePath, newline="") as file:
    data = csv.reader(file, delimiter=",")

    # Reading the header row first
    Header = next(file)

    # Reading through each row
    for row in data:
        Candidates.append(row[2])

    # Sorting the list of candidates
    SortedCandidates = sorted(Candidates)

    # Counting votes per candidate
    CandidateCount = Counter(SortedCandidates)
    VotesPerCandidate.append(CandidateCount.most_common())

    # Calculating percentages
    for item in VotesPerCandidate:
        first = format((item[0][1]) * 100 / (sum(CandidateCount.values())), '.3f')
        second = format((item[1][1]) * 100 / (sum(CandidateCount.values())), '.3f')
        third = format((item[2][1]) * 100 / (sum(CandidateCount.values())), '.3f')
        fourth = format((item[3][1]) * 100 / (sum(CandidateCount.values())), '.3f')

#  Printing the analysis to terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes:  {sum(CandidateCount.values())}")
print("-------------------------")
print(f"{VotesPerCandidate[0][0][0]}: {first}% ({VotesPerCandidate[0][0][1]})")
print(f"{VotesPerCandidate[0][1][0]}: {second}% ({VotesPerCandidate[0][1][1]})")
print(f"{VotesPerCandidate[0][2][0]}: {third}% ({VotesPerCandidate[0][2][1]})")
print(f"{VotesPerCandidate[0][3][0]}: {fourth}% ({VotesPerCandidate[0][3][1]})")
print("-------------------------")
print(f"Winner:  {VotesPerCandidate[0][0][0]}")
print("-------------------------")

# Exporting to a text file
with open(OutputFilePath, "w") as outfile:
    outfile.write("Election Results\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Total Votes:  {sum(CandidateCount.values())}\n")
    outfile.write("-------------------------\n")
    outfile.write(f"{VotesPerCandidate[0][0][0]}: {first}% ({VotesPerCandidate[0][0][1]})\n")
    outfile.write(f"{VotesPerCandidate[0][1][0]}: {second}% ({VotesPerCandidate[0][1][1]})\n")
    outfile.write(f"{VotesPerCandidate[0][2][0]}: {third}% ({VotesPerCandidate[0][2][1]})\n")
    outfile.write(f"{VotesPerCandidate[0][3][0]}: {fourth}% ({VotesPerCandidate[0][3][1]})\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Winner:  {VotesPerCandidate[0][0][0]}\n")
    outfile.write("-------------------------\n")
