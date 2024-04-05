

    # Create a Python script that analyzes the PyBank records to calculate each of the following:
# -->>  The total number of months included in the dataset
# -->>  The net total amount of "Profit/Losses" over the entire period
# -->>  The average of the changes in "Profit/Losses" over the entire period
# -->>  The greatest increase in profits (date and amount) over the entire period
# -->>  The greatest decrease in losses (date and amount) over the entire period
# -->>  Print the analysis to the terminal and export a text file with the results


# Import dependencies
import os
import csv

# Define PyBank's variables
Months = []
ProfitAndLossChanges = []

MonthsCounter = 0
TotalProfitAndLoss = 0
PreviousMonthProfitAndLoss = 0
CurrentMonthProfitAndLoss = 0
ProfitAndLossChange = 0


# Change directory to the directory of current python script
os.chdir(os.path.dirname(__file__))

# Path to collect data from the Resources folder
budget_dat_csv_path = os.path.join("Resources", "budget_data.csv")


# Open and read csv
#BudgetDataCsvPath = os.path.join("Resources", "budget_data.csv")
#BudgetDataCsvPath = os.path.join("Resources", "budget_data.csv")
with open(budget_dat_csv_path, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvfile)

    #print(f"Header: {csv_header}")
    # This prints -->> Header: Date, Profit/Losses
             
    # Read through each row of data after the header
    for row in csv_reader:

        # Count of months
        MonthsCounter += 1

        # Net total amount of "Profit/Losses" over the entire period
        CurrentMonthProfitAndLoss = int(row[1])
        TotalProfitAndLoss += CurrentMonthProfitAndLoss

        if (MonthsCounter == 1):
            # Make the value of previous month to be equal to current month
            PreviousMonthProfitAndLoss = CurrentMonthProfitAndLoss
            continue

        else:

            # Compute change in profit loss 
            ProfitAndLossChange = CurrentMonthProfitAndLoss - PreviousMonthProfitAndLoss

            # Append each month to the months[]
            Months.append(row[0])

            # Append each profit_loss_change to the profit_loss_changes[]
            ProfitAndLossChanges.append(ProfitAndLossChange)

            # Make the current_month_loss to be previous_month_profit_loss for the next loop
            PreviousMonthProfitAndLoss = CurrentMonthProfitAndLoss
    #sum and average of the changes in "Profit/Losses" over the entire period
    SumProfitAndLoss = sum(ProfitAndLossChanges)
    AverageProfitAndLoss = round(SumProfitAndLoss/(MonthsCounter - 1), 2)

    # highest and lowest changes in "Profit/Losses" over the entire period
    HighestChange = max(ProfitAndLossChanges)
    LowestChange = min(ProfitAndLossChanges)

    # Locate the index value of highest and lowest changes in "Profit/Losses" over the entire period
    HighestMonthIndex = ProfitAndLossChanges.index(HighestChange)
    LowestMonthIndex = ProfitAndLossChanges.index(LowestChange)

    # Assign best and worst month
    BestMonth = Months[HighestMonthIndex]
    WorstMonth = Months[LowestMonthIndex]

# -->>  Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {MonthsCounter}")
print(f"Total:  ${TotalProfitAndLoss}")
print(f"Average Change:  ${AverageProfitAndLoss}")
print(f"Greatest Increase in Profits:  {BestMonth} (${HighestChange})")
print(f"Greatest Decrease in Losses:  {WorstMonth} (${LowestChange})")


# -->>  Export a text file with the resultsf
budget_file = os.path.join("Output", "budget_data.txt")
with open(budget_file, "w") as outfile:

    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months:  {MonthsCounter}\n")
    outfile.write(f"Total:  ${TotalProfitAndLoss}\n")
    outfile.write(f"Average Change:  ${AverageProfitAndLoss}\n")
    outfile.write(f"Greatest Increase in Profits:  {BestMonth} (${HighestChange})\n")
    outfile.write(f"Greatest Decrease in Losses:  {WorstMonth} (${LowestChange})\n")