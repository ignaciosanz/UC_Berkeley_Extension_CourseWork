
import os
import csv

#create output text file
text_file = open("Output_Exercise1.txt", "w")


# Path to collect data from the Resources folder
#wrestlingCSV = os.path.join('budget_data.csv')
budgetDataCSV = os.path.join('02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv')

dates = []

monthAgregator = []

difference = []

# Read in the CSV file
with open(budgetDataCSV, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    #this variable stores the number of months, which is the number of rows
    monthsCounter = 0

    #this variable stores the sum of profit/loss by adding column one of that data
    sumTotalProfit = 0.0

    #this is a place holder to store the previous number in order to caculate the 
    #change between the two values
    previousNumber = 0.0

    # Loop through the data
    for row in csvreader:

        monthsCounter = monthsCounter + 1

        sumTotalProfit = float(row[1]) + sumTotalProfit

        monthAgregator.append(row[1])

        dates.append(row[0])

        #difference.append(previousNumber - float(row[1]))
        difference.append(float(row[1]) - previousNumber)

        previousNumber = float(row[1])


#pring restuls into out text file
text_file.write("Financial Analysis\n------------------------\n")
text_file.write(f"Total months: {str(monthsCounter)}\n")
text_file.write(f"Total: {str(sumTotalProfit)}\n")

#print out results into console
print("Financial Analysis\n------------------------")
print(f"Total months: {str(monthsCounter)}")
print(f"Total: {str(sumTotalProfit)}")


#the first value of the difference list is not valid becuase there is no
#value before the fist row to calculte the difference
difference.pop(0)


text_file.write(f"Average  Change: $ {sum(difference)/len(difference)}\n")
#the lenght of difference is needed to caludate the average change
print(f"Average  Change: $ {sum(difference)/len(difference)}")


min_value = min(difference)
max_value = max(difference)
#need to add two to the index.max because first row is headers and also i removed the first row form
#the difference list when calculating the average change
max_index = difference.index(max_value) + 2
min_index = difference.index(min_value) + 2


text_file.write(f"Greatest Increase in Profits: {dates[(max_index - 1)]} (${str(max_value)})\n")
#print(f"{wrestlerData[0]} is a {typeOfWrestler}")
print(f"Greatest Increase in Profits: {dates[(max_index - 1)]} (${str(max_value)})")

text_file.write(f"Greatest Decrease in Profits: {dates[(min_index - 1)]} (${str(min_value)})")
print(f"Greatest Decrease in Profits: {dates[(min_index - 1)]} (${str(min_value)})")


#close output text file
text_file.close()
