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

# Open the election results and read the file.
with open(file_to_load) as election_data:
    
    #To do: read and analyze the data here.
    file_reader =  csv.reader(election_data)
    headers = next (file_reader)
    print(headers)
    for row in file_reader:
        print(row)