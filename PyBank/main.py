import os
import csv

bank_csv = os.path.join("/Users/adora/Desktop/BOOTCAMP_ASSIGNMENTS/Python_challenge/Python-challenge/PyBank/Resources/budget_data.csv")

# Open and read csv file
with open(bank_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
# Read header    
    csv_header = next(csv_file)
    
    x =[]
    y =[]
    
    for row in csv_reader:
        Date = row[0]
        Profit_Losses = int(row[1])
        x.append(Date)
        y.append(Profit_Losses)
# total number of months included in the dataset
total_months = len(set(x))
        
# net total amount of "Profit/Losses" over the entire period
entire_total_amount = sum(y)

# changes in "Profit/Losses" over the entire period, and then the average of those changes, greatest increase and decrease

changes_profit_loss = [y[i] - y[i - 1] 
           for i in range(1, len(y))]
average = sum(changes_profit_loss)/ len(changes_profit_loss)
average_changes = round(average, 2)

greatest_increase = max(changes_profit_loss)
greatest_decrease = min(changes_profit_loss)

greatest_increase_index = changes_profit_loss.index(greatest_increase) + 1
greatest_decrease_index = changes_profit_loss.index(greatest_decrease) + 1

greatest_increase_date = x[greatest_increase_index]
greatest_decrease_date = x[greatest_decrease_index]



# final output-----------------------------------------------------------------
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${entire_total_amount}")
print(f"Average Change: ${average_changes}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

   
   
   
   
