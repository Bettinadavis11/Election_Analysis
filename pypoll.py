# Add our dependencies
import os
import csv

# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Candidate options and candidate votes.
total_votes=0
candidate_options=[]
candidate_votes={}

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers=next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        #If the candidate does not mathc any existing candidate, add the number to the candidate list.
        if candidate_name not in candidate_options:
        
        # Add the candidate name to the candidate list.
         candidate_options.append(candidate_name)

        # Begin tracking that candidate's vote count.
         candidate_votes[candidate_name] = 0
          
        # Add a vote to that candidate's count
         candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save,'w') as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    # Print(election_results, end="")
    txt_file.write(election_results)
    
# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
    for candidate in candidate_votes:
        #2. Retrieve vote count of a candidate
        votes=candidate_votes[candidate]
        #3. Calcuate the percentage of votes
        vote_percentage=round((float(votes)/total_votes)*100,1)

        if (votes>winning_count) and (vote_percentage>winning_percentage):
            winning_count=votes
            winning_percentage=vote_percentage
            winning_candidate=candidate        

        candidate_results=(f"{candidate}: {vote_percentage}% ({votes:,})\n")
        txt_file.write(candidate_results)


    # Print the candidate winner
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

     # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)