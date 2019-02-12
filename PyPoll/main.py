#Import os module to create file path across operating systems
import os

#Module for reading csv file
import csv

#Create the lists to store data.
count = 0
candidatelist = []
unique_candidate = []
vote_count = []
vote_percent = []

#Open the csv
csvpath = os.path.join('..','election_data.csv')


#Create the lists to store data.
count = 0
candidatelist = []
unique_candidate = []
vote_count = []
vote_percent = []


#Reading using csv module
with open(csvpath, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    #Conduct ask
    for row in csvreader:

        # Count the total number of votes
        count = count + 1

        # Set the candidate names to candidatelist

        candidatelist.append(row[2])

        # Create a set from the candidatelist to get the unique candidate names

    for x in set(candidatelist):

        unique_candidate.append(x)

        # y is the total number of votes per candidate

        y = candidatelist.count(x)

        vote_count.append(y)

        # z is the percent of total votes per candidate

        z = round(((y/count)*100),2)

        vote_percent.append(z)



    winning_vote_count = max(vote_count)

    winner = unique_candidate[vote_count.index(winning_vote_count)]


print("-------------------------")

print("Election Results")

print("-------------------------")

print("Total Votes :" + str(count))

print("-------------------------")

for i in range(len(unique_candidate)):

            print(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i])+ ")")

print("-------------------------")

print("The winner is: " + winner)

print("-------------------------")



# Print to a text file: election_results.txt

with open('election_results.txt', 'w') as text:

    text.write("Election Results\n")

    text.write("---------------------------------------\n")

    text.write("Total Vote: " + str(count) + "\n")

    text.write("---------------------------------------\n")

    for i in range(len(set(unique_candidate))):

        text.write(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i]) + ")\n")

    text.write("---------------------------------------\n")

    text.write("The winner is: " + winner + "\n")

    text.write("---------------------------------------\n")

=======
#Import os module to create file path across operating systems
import os

#Module for reading csv file
import csv

#Create the lists to store data.
count = 0
candidatelist = []
unique_candidate = []
vote_count = []
vote_percent = []

#Open the csv
csvpath = os.path.join('..','election_data.csv')


#Create the lists to store data.
count = 0
candidatelist = []
unique_candidate = []
vote_count = []
vote_percent = []


#Reading using csv module
with open(csvpath, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    #Conduct ask
    for row in csvreader:

        # Count the total number of votes
        count = count + 1

        # Set the candidate names to candidatelist

        candidatelist.append(row[2])

