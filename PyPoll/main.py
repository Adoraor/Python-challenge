from collections import Counter
import os
import csv

csv_file_path = 'Resources/election_data.csv'
script_directory = os.path.dirname(os.path.abspath(__file__))
poll_csv = os.path.join(script_directory, csv_file_path)


ballot_ids = []
counties = []
candidates = []

# Open and read csv file
with open(poll_csv) as poll_file:
    csv_reader = csv.reader(poll_file, delimiter = ",")
    # Read header    
    csv_header = next(poll_file)
    
    for row in csv_reader:
        ballot_id = str(row[0])
        county = row[1]
        candidate = row [2]
        ballot_ids.append(ballot_id)
        counties.append(county)
        candidates.append(candidate)


# The total number of votes cast
total_votes = len(ballot_ids)
candidates_voted = set(candidates)
vote_count = Counter(candidates)

#export to text file
with open('/Users/adora/Desktop/BOOTCAMP_ASSIGNMENTS/Python_challenge/Python-challenge/PyPoll/analysis/election.txt', 'w') as f:
    f.write('Election Results\n')
    f.write('-------------------------\n')
    f.write(f'Total Votes: {total_votes}\n')
    f.write('-------------------------\n')

    for candidate, count in vote_count.items():
        percentage = (count / total_votes) * 100
        vote_percentage = f" {candidate}: {percentage:.3f}% ({count})\n\n"
        f.write(vote_percentage)
    winner = (vote_count.most_common()[0][0])
    f.write('-------------------------\n')
    f.write(f'Winner: {winner}\n')

    f.write('-------------------------\n')


#print in terminal
print ('Election Results')
print('-------------------------')
print(f'Total Votes: {total_votes}')
print('-------------------------')

for candidate, count in vote_count.items():
        percentage = (count / total_votes) * 100
        vote_percentage = f" {candidate}: {percentage:.3f}% ({count})"
        print(vote_percentage)
        winner = (vote_count.most_common()[0][0])
print('-------------------------')
print(f'Winner: {winner}')

print('-------------------------')