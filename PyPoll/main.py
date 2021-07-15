# import dependencies
import csv
import os

# set filepath
fpath = os.path.join("Resources", "election_data.csv")


# global variables as needed
ed_candidate_col = []
tot_votes = 0
candidate_list = []
counter = 0
vote_count = {}
vote_percent = {}


# open and read information
with open(fpath) as ed_csv:
    ed_reader = csv.reader(ed_csv, delimiter=",")
    next(ed_reader, None)
    for r in ed_reader:
        ed_candidate_col.append(r[2])

# calculate total number of votes cast
    tot_votes = len(ed_candidate_col)
    #print(tot_votes)

# list of candidates who received votes

    for r in ed_candidate_col:
        if r not in candidate_list:
            candidate_list.append(r)
    #print(candidate_list)


# assign total number of votes each candidate won
    c_indx = 0
    for c in candidate_list:
        for r in ed_candidate_col:
            if r == c:
                counter += 1
        #print(f"Candidate {c} won {counter} votes.")
        c_indx += 1
        vote_count[c] = counter
        counter = 0
    #print(vote_count)

# assign total percentage of votes each candidate won
    for c in candidate_list:
        vote_percent[c] = vote_count[c]/tot_votes
    #print(vote_percent)

# winner based on popular vote
    most_votes = (max(vote_count.values()))
    pop_vote_win = (list(vote_count.keys()))[list(vote_count.values()).index(most_votes)]
    #print(most_votes)
    #print(pop_vote_win)

# print analysis to terminal and text file

print(f"Election Results\n-----------------------\nTotal Votes: {tot_votes}\n-----------------------")
for c in candidate_list:
    print(f"{c}: {(vote_percent[c]):.3%} ({vote_count[c]})")
print(f"-----------------------\nWinner: {pop_vote_win}\n-----------------------")

f = open("analysis/analysis.txt", "w")
f.write(f"Election Results\n-----------------------\nTotal Votes: {tot_votes}\n-----------------------\n")
for c in candidate_list:
    f.write(f"{c}: {(vote_percent[c]):.3%} ({vote_count[c]})\n")
f.write(f"-----------------------\nWinner: {pop_vote_win}\n-----------------------")
f.close()