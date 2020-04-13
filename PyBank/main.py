# Importing dependencies
import os
import csv

# Setting directory to the script file
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
# Input path file
budget_data_csv_path = os.path.join("Resources", "budget_data.csv")
# Output path file
budget_file = os.path.join("Results", "output.txt")

# variables
Months = []
ProfitLoss = []
TotalMonths = 0
NetProfitLoss = 0
PrevMonthPL = 0
CurrentMonthPL = 0
ChangeProfitLoss = 0


# Opening and reading csv file
with open(budget_data_csv_path, newline="") as file:

    data = csv.reader(file, delimiter=",")

    # Read the header row first
    csv_header = next(file)

    # Read through each row of data after the header
    for row in data:

        # total months
        TotalMonths += 1

        # Net Profit or Loss
        CurrentMonthPL = int(row[1])
        NetProfitLoss += CurrentMonthPL

        if TotalMonths == 1:
            PrevMonthPL = CurrentMonthPL
            continue

        else:
            # change in profit loss
            ChangeProfitLoss = CurrentMonthPL - PrevMonthPL

            # Appending to Months
            Months.append(row[0])

            # Append to ChangeProfitLoss
            ProfitLoss.append(ChangeProfitLoss)

            # Making previous month's Profit/Lss current ones
            PrevMonthPL = CurrentMonthPL

    # Sum and Average of Profit/Loss
    TotalProfitLoss = sum(ProfitLoss)
    AverageProfitLoss = round(TotalProfitLoss / (TotalMonths - 1), 2)

    # Maximum and Minimum Change
    MaxChange = max(ProfitLoss)
    MinChange = min(ProfitLoss)

    # Index of Max and Min value
    IndexOfMax = ProfitLoss.index(MaxChange)
    IndexOfMin = ProfitLoss.index(MinChange)

    # Assign best and worst month
    BestMonth = Months[IndexOfMax]
    WorstMonth = Months[IndexOfMin]

# Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {TotalMonths}")
print(f"Total:  ${NetProfitLoss}")
print(f"Average Change:  ${AverageProfitLoss}")
print(f"Greatest Increase in Profits:  {BestMonth} (${MaxChange})")
print(f"Greatest Decrease in Losses:  {WorstMonth} (${MinChange})")


# Export a text file with the results
with open(budget_file, "w") as outfile:

    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months:  {TotalMonths}\n")
    outfile.write(f"Total:  ${NetProfitLoss}\n")
    outfile.write(f"Average Change:  ${AverageProfitLoss}\n")
    outfile.write(f"Greatest Increase in Profits:  {BestMonth} (${MaxChange})\n")
    outfile.write(f"Greatest Decrease in Losses:  {WorstMonth} (${MinChange})\n")