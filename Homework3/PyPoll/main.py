import os
import csv
#import collections to access the Counter method 
import collections

#creat output text file
text_file = open("Output_Exercise2.txt", "w")


#Path to collect data from the Resources folder
#wrestlingCSV = os.path.join('budget_data.csv')
electionDataCSV = os.path.join('02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv')


#this list holds all of the votes. This list is pass into the
#collections.counter method to generate a library where the name of the candidates
#are the keys and the count of names are the values. E.g. Khan: 2343 votes. 
votes = []

#this list holds a distinct list of candidates
candidates = []

#this list is for adding the sum of all votes per candidate inside the while loop.
#this list is to be used for finding the winner
WinnerList = []

#used for the while loop
Counter3 = 0

#this variable stores the number of months, which is the number of rows
TotalVotes = 0



# Read in the CSV file
with open(electionDataCSV, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)



    # Loop through each row of the data set
    for row in csvreader:
        #add 1 to TotalVotes variable calculate the total number of votes
        TotalVotes = TotalVotes + 1


        #find distinct candidates from data set and append the names into the candidate list
        if row[2] not in candidates:
            candidates.append(row[2])
        
        #append each vote to the votes list. This list will be passed into the
        #collections.counter method to generate a library        
        votes.append(row[2])


#print results into out text file
text_file.write(f"Election Results\n----------------\nTotal Votes: {TotalVotes}\n----------------\n")

#print results into console
print("Election Results")
print("---------------------")
print(f"Total Votes: {TotalVotes}")
print("---------------------")
   


#Counter3 needs to be the lenght of the candidates list.
#need remove 1 from the len(candidates) becuase first index stars
#with 0, not 1.
Counter3 = len(candidates) - 1 

#create a dictonary where the candidate names are they keys and the number of votes per candidate are the values
dictionary = collections.Counter(votes)

#this while loop will run for as many times as the lenght of the candidates list
#the votes list is handed to the collections.counter method for generating a 
#libray with the candidate names as keys and the count of names as values
#the loop prints the candidates name, calculates the percentage and print the actual value
#all within the print statement     
while Counter3 != -1:
    
    #get the value from the dictonary for candidate index Counter3.
    variable = dictionary.get(candidates[Counter3], None)
    print(f"{candidates[Counter3]}: {(variable*100)/TotalVotes}% ({str(variable)})")
    #pring to output text file
    text_file.write(f"{candidates[Counter3]}: {(variable*100)/TotalVotes}% ({str(variable)})\n")
    WinnerList.append(variable)
    Counter3 = Counter3 - 1

#reverse list conatining the count of votes per candidate in order to match
#indexes from the candidate list. Need both lists to match indexes
#for calculating the winner.
WinnerList.reverse()

print("---------------------")
#print out the winner candiadte by using the max function in the winnerlist.
#the winnerlist contains each of the total values each candidate in the 
#same order as the candidate list. Getting the index of the highest value
#can be used as the index for the candidates list to identify the name of the
#winner candidate
print(f"Winner: {candidates[WinnerList.index(max(WinnerList))]}")
print("---------------------")

#print result into output text file
text_file.write(f"----------------\n")
text_file.write(f"Winner: {candidates[WinnerList.index(max(WinnerList))]}")

#close output text file
text_file.close()
