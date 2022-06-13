# The data we need to retrieve.
# Recources/election_results.csv
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

# Add our dependencies.
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Initialize empty list for candidate names
candidate_options = []

# Initialize empty dictionary for counting votes
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        
        # Print the candidate name from each row
        candidate_name = row[2]
        # If candidate name not already on list...
        if candidate_name not in candidate_options:
            # Add unique names to candidate list.
            candidate_options.append(candidate_name)
            # Begin tracking candidate's vote count
            candidate_votes[candidate_name] = 0
        # Add a vote to candidate's count
        candidate_votes[candidate_name] += 1

# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list.
for candidate_name in candidate_votes:
    # Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    #To do: print out each candidate's name, vote count, and percentage of votes to terminal.
    with open(file_to_save, "w") as txt_file:
            txt_file.write(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    # Determine winning vote count and candidate
    # Determine if votes are greater than the winning count.
    if votes > winning_count and (vote_percentage > winning_percentage):
        # If true, set winning_count = votes and winning_percent = vote_percent
        winning_count = votes
        winning_percentage = vote_percentage
        # Set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"--------------------------\n")

# To do: print out the winning candidate, vote count and percentage to terminal.
# with open(file_to_save, "w") as txt_file:
    # txt_file.write(winning_candidate_summary)    
    
    # Print the candidate name and percentage of votes.
    # print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")



# Print the candidate list.
# print(candidate_votes)

# Print the total votes.
# print(total_votes)

# Use the with statement to open the file as a text file.
# with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    # txt_file.write("Counties in the election\n-------------------------\nArapahoe\nDenver\nJefferson")