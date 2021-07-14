# import budget data
import os
import csv
from operator import itemgetter


fpath = os.path.join("Resources", "budget_data.csv")

bd_rows = {}
months = 0
net_tot_amt = 0
change = 0
change_list = {}
change_tot = 0
aver_change = 0
greatest_inc = {}
greatest_dec = {}

with open(fpath) as bd_csv:
    bd_reader = csv.reader(bd_csv, delimiter=",")
    for r in bd_reader:
        bd_rows[r[0]] = r[1]

# The total number of months included in the dataset
    months = len(list(bd_rows)) - 1
    #print (f"{months}")

# The net total amount of "Profit/Losses" over the entire period
    bd_csv.seek(0)
    next(bd_reader)

    net_tot_amt = sum(int(r[1]) for r in bd_reader)
    #print(net_tot_amt)

# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
    bd_csv.seek(0)
    next(bd_reader)
    count = 0
    for r in bd_reader:
        if count == 0:
            first = int(r[1])
        else:         
            second = int(r[1])
            change = second - first
            change_list[count] = change
            change_tot += change
            first = second
        count += 1
    aver_change = round(change_tot/(months-1), 2)
    #print(aver_change)

# The greatest increase in profits (date and amount) over the entire period
    amount = max(change_list.items(), key=itemgetter(1))
    date = list(bd_rows)
    greatest_inc[date[amount[0]+1]] = amount[1]
    #print(greatest_inc)

# The greatest decrease in profits (date and amount) over the entire period
    amount = min(change_list.items(), key=itemgetter(1))
    date = list(bd_rows)
    greatest_dec[date[amount[0]+1]] = amount[1]
    #print(greatest_dec)

print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {months}")
print(f"Total: {net_tot_amt}")
print(f"Average Change: {aver_change}")
for key,value in greatest_inc.items():
    print(f"Greatest Increase in Profits: {key} (${value})")
for key,value in greatest_dec.items():
    print(f"Greatest Decrease in Profits: {key} (${value})")

f = open("analysis/analysis.txt", "w")
f.write(f"Financial Analysis\n-----------------------------\nTotal Months: {months}\nTotal: {net_tot_amt}\nAverage Change: {aver_change}\n")
for key,value in greatest_inc.items():
    f.write(f"Greatest Increase in Profits: {key} (${value})\n")
for key,value in greatest_dec.items():
    f.write(f"Greatest Decrease in Profits: {key} (${value})\n")
f.close()