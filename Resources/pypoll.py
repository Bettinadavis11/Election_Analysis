#Assign a variable for the file to load and a path.
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("Analysis" "election_Analysis.txt")
outfile = open(file_to_save, "w")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)
outfile.close()

with open(file_to_save, "w") as txt_file:
    txt_file.write("counties in the Election\n")
    txt_file.write(("-" * 10) + "\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")

txt_file.close()

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate options and candidate votes
candidate_options = []
# 1. Declare the empty dictionary.
candidate_votes = {}

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        if candidate_name not in candidate_options:
          # Add the candidate name to the candidate list.
          candidate_options.append(candidate_name)

          # 2. Begin tracking that candidate's vote count.
          candidate_votes[candidate_name] = 0
          # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Print the candidate vote dictionary.
print(total_votes)
print(candidate_options)
print(candidate_votes)

winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

    if(votes > winning_count) and (vote_percentage > winning_percentage):
       winning_count = votes
       winning_percentage = vote_percentage
       winning_candidate = candidate_name

    # 4. Print the candidate name and percentage of votes.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    winning_candidate_summary = (
        f"Winner: {winning_candidate}"
        f"winning Vote Count {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------------\n"
    )

    print(winning_candidate_summary)
