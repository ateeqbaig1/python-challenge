# Importing dependencies
import os
import csv
import _collections
from _collections import _count_elements

# Setting directories
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
# Input file path
InputFilePath = os.path.join("Resources", "elections_data.csv")
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

    # count votes per candidate in most common outcome order and append to a list
    CandiateCount = _count_elements(SortedCandidates)
    VotesPerCandidate.append(CandiateCount.most_common())

    # calculate the percentage of votes per candicate in 3 digital points
    for item in VotesPerCandidate:
        first = format((item[0][1]) * 100 / (sum(CandiateCount.values())), '.3f')
        second = format((item[1][1]) * 100 / (sum(CandiateCount.values())), '.3f')
        third = format((item[2][1]) * 100 / (sum(CandiateCount.values())), '.3f')
        fourth = format((item[3][1]) * 100 / (sum(CandiateCount.values())), '.3f')



# -->>  Print the analysis to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes:  {sum(CandiateCount.values())}")
print("-------------------------")
print(f"{VotesPerCandidate[0][0][0]}: {first}% ({VotesPerCandidate[0][0][1]})")
print(f"{VotesPerCandidate[0][1][0]}: {second}% ({VotesPerCandidate[0][1][1]})")
print(f"{VotesPerCandidate[0][2][0]}: {third}% ({VotesPerCandidate[0][2][1]})")
print(f"{VotesPerCandidate[0][3][0]}: {fourth}% ({VotesPerCandidate[0][3][1]})")
print("-------------------------")
print(f"Winner:  {VotesPerCandidate[0][0][0]}")
print("-------------------------")

# -->>  Export a text file with the results

with open(OutputFilePath, "w") as outfile:
    outfile.write("Election Results\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Total Votes:  {sum(CandiateCount.values())}\n")
    outfile.write("-------------------------\n")
    outfile.write(f"{VotesPerCandidate[0][0][0]}: {first}% ({VotesPerCandidate[0][0][1]})\n")
    outfile.write(f"{VotesPerCandidate[0][1][0]}: {second}% ({VotesPerCandidate[0][1][1]})\n")
    outfile.write(f"{VotesPerCandidate[0][2][0]}: {third}% ({VotesPerCandidate[0][2][1]})\n")
    outfile.write(f"{VotesPerCandidate[0][3][0]}: {fourth}% ({VotesPerCandidate[0][3][1]})\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Winner:  {VotesPerCandidate[0][0][0]}\n")
    outfile.write("-------------------------\n")