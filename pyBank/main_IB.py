# 1.total number of months
import os
import csv
import numpy as np

buget_file = os.path.join("","Resources","budget_data.csv")
total_months = 0
Total_Net_profit_losses = 0
previous_month = ''
current_month = ''
profit_change = 0
previous_month_value = 0 
sum_profit_change = 0
profit_list = []
profit_change_list = []
change = 0
Dictn_profit_change = {}
lowest_month = ''
highest_month = ''
greatest_decrease = 0
greatest_increase = 0
profit_months=[]

with open(buget_file, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        total_months +=1
        Net_profit_losses = int(row[1])
        Total_Net_profit_losses += Net_profit_losses
        current_month = row[0]
        current_month_value = int(row[1])
        #storing current month value in profit list
        profit_list.append(current_month_value)
        #storing current & previous months in month list
        profit_months.append(str(previous_month+current_month))


# calculate profit change and store in  dictionary

Dictn_profit_change={}

for i in range(0, len(profit_list)-1):
    if i > 0:
        change = int(profit_list[i+1]) - int(profit_list[i])
        changemonth= profit_months[i+1] 
        
        Dictn_profit_change.update({change: changemonth})
        if change > greatest_increase: 
            greatest_increase = change
        if change < greatest_decrease: 
            greatest_decrease = change
        


print(Dictn_profit_change[greatest_decrease] + " : "+ '${:}'.format(str(greatest_decrease)) + " Greatest decrease")
print(Dictn_profit_change[greatest_increase] + " : "+ '${:}'.format(str(greatest_increase)) + " Greatest increase")

print("Average change: " + '${:.2f}'.format((profit_list[len(profit_list)-1] - profit_list[0])/85))

print("Total months: " + str(total_months))
print("Total: " + '${:.2f}'.format(Total_Net_profit_losses))

print("Writing output text file")

output_path = os.path.join("", "Pnl_Analysis.txt")
out = open(output_path,"w")
out.write(Dictn_profit_change[greatest_decrease] + " : "+ '${:}'.format(str(greatest_decrease)) + " Greatest decrease\n")
out.write(Dictn_profit_change[greatest_decrease] + " : "+ '${:}'.format(str(greatest_decrease)) + " Greatest decrease\n")
out.write(Dictn_profit_change[greatest_increase] + " : "+ '${:}'.format(str(greatest_increase)) + " Greatest increase\n")
out.write("Average change: " + '${:.2f}\n'.format((profit_list[len(profit_list)-1] - profit_list[0])/85))
out.write("Total months: " + str(total_months) + "\n")
out.write("Total: " + '${:.2f}\n'.format(Total_Net_profit_losses))
out.close()
 





    