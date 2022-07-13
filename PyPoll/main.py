# Python script to analyze election data.
# import file
import os
import csv
file_path = os.path.join('Resources','election_data.csv')
# create variables & empty lists to store values
total_votes = 0
candidates = []
candidate_names = []
# read the file
with open(file_path) as election_data:
        csv_reader=csv.reader(election_data,delimiter=',')
        # read header row first
        csv_header=next(election_data)
        # loop through the data, counting the number of votes and adding candidates
        # to their own list
        for row in csv_reader:
                total_votes = total_votes +1
                candidates.append(row[2])
        # loop through all the candidates listed to create new list with unique
        # values only code used from favtutor.com/blogs/remove-duplicates-from-
        # list-python
        [candidate_names.append(x) for x in candidates if x not in candidate_names]
# create variables for number of votes per candidate & percentage of votes received
c_votes = candidates.count('Charles Casper Stockham')
d_votes = candidates.count('Diana DeGette')
r_votes = candidates.count('Raymon Anthony Doane')
c_percent = str(round(c_votes/total_votes*100,3))+'%'
d_percent = str(round(d_votes/total_votes*100,3))+'%'
r_percent = str(round(r_votes/total_votes*100,3))+'%'
# create dictionary to print
dictionary = {'Charles Casper Stockham': f"{c_percent} ({c_votes})",
              'Diana DeGette': f"{d_percent} ({d_votes})",
              'Raymon Anthony Doane': f"{r_percent} ({r_votes})"}
#print analysis
print(f'''Election Results
-------------------------
Total Votes: {total_votes}
-------------------------''')
# print dictionary showing each candidate on their own line, code used from
# thispointer.com/python-4-ways-to-print-items-of-a-dictionary-line-by-line/
for key, value in dictionary.items():
        print(key, ':', value)
print("-------------------------")
# determine and print the winner
if c_votes>d_votes and c_votes>r_votes:
        print("Winner: Charles Casper Stockham")
elif d_votes>c_votes and d_votes>r_votes:
        print("Winner: Diana DeGette")
else: 
        print("Winner: Raymon Anthony Doane")
print("-------------------------")
# write results to a txt file
with open('election_analysis.txt','w') as f:
        print(f'''Election Results
-------------------------
Total Votes: {total_votes}
-------------------------''', file = f)
        for key, value in dictionary.items():
                print(key, ':', value, file = f)
        print("-------------------------", file = f)
        if c_votes>d_votes and c_votes>r_votes:
                print("Winner: Charles Casper Stockham", file = f)
        elif d_votes>c_votes and d_votes>r_votes:
                print("Winner: Diana DeGette", file = f)
        else: 
                print("Winner: Raymon Anthony Doane", file = f)
        print("-------------------------", file = f)
