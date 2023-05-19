import os
import csv

bank_csv = os.path.join("/Users/adora/Desktop/BOOTCAMP_ASSIGNMENTS/Python_challenge/Python-challenge/PyBank/Resources/budget_data.csv")

# Open and read csv file
with open(bank_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
# Read header    
    csv_header = next(csv_file)
    
    Dates =[]
    Profit_Losses =[]
    
    for row in csv_reader:
        Date = row[0]
        Profit_Loss = int(row[1])
        Dates.append(Date)
        Profit_Losses.append(Profit_Loss)
# total number of months included in the dataset
total_months = len(set(Dates))
        
# net total amount of "Profit/Losses" over the entire period
entire_total_amount = sum(Profit_Losses)

# changes in "Profit/Losses" over the entire period, and then the average of those changes, greatest increase and decrease

changes_profit_loss = [Profit_Losses[i] - Profit_Losses[i - 1] 
           for i in range(1, len(Profit_Losses))]
average = sum(changes_profit_loss)/ len(changes_profit_loss)
average_changes = round(average, 2)

greatest_increase = max(changes_profit_loss)
greatest_decrease = min(changes_profit_loss)

greatest_increase_index = changes_profit_loss.index(greatest_increase) + 1
greatest_decrease_index = changes_profit_loss.index(greatest_decrease) + 1

greatest_increase_date = Dates[greatest_increase_index]
greatest_decrease_date = Dates[greatest_decrease_index]

with open('/Users/adora/Desktop/BOOTCAMP_ASSIGNMENTS/Python_challenge/Python-challenge/PyBank/analyis/bank.txt', 'w') as f:
    f.write('Financial Analysis\n')
    f.write('----------------------------\n')
    f.write(f'Total Months: {total_months}\n')
    f.write(f'Total: ${entire_total_amount}\n')
    f.write(f'Average Change: ${average_changes}\n')
    f.write(f'Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n')
    f.write(f'Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n')

   
   
   
   
