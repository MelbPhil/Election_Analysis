# Election_Analysis

## Automating an election audit with Python

### Overview of Election Audit
I assited a Colorado Board of Elecitons employee in writing a python script for analysing and printing the tabulated results of a US congressional precinct in Colorado. The script needed to be able to perform the following tasks:

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Get a complete list of the counties that participated in the election.
4. Calculate the total number of votes each candidate received.
5. Calculate the voter turnout for each county.
6. Calculate the percentage of votes each county receieved out of the total count.
7. Determine the county with the highest turnout.
8. Calculate the percentage of votes each candidate won.
9. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.9.12, Visual Studio Code, 1.68.0

## Election-Audit Results
The analysis of the election shows that:
- There were 369,711 votes cast in the election
- The voter turnout for each county in the precinct:
    - Jefferson: 10.5% (38,855)
    - Denver: 82.8% (306,055)
    - Arapahoe: 6.7% (24,801)
- The county with the highest voter turnout: Denver
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 votes.
    - Diana DeGette received 73.8% of the vote and 272,892 votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes.
- The winner of the election was:
    - Diana DeGette, who received 73.8% of the vote and 272,892 votes.

## Election-Audit Summary
The python script created for this election is quite valuable as it can be easily repurposed (_with a few slight modifications_) to assist with analysing the results of any future elections. For the purpose of explanation, let's pretend we need to repurpose this script to tally the results of a Senate Primary Election. 

First and foremost, we must adjust the file path `file_to_load = os.path.join("Desktop", "Class_work", "Week_3_Python", "Election_Analysis", "Resources", "election_results.csv")` ensuring that we're pulling data from the appropriate CSV file containing the data for the Senate Primary Election. Likewise, we must be consciencous of where we will be saving the script's analysis results, adjusting the code `file_to_save = os.path.join("Desktop", "Class_work", "Week_3_Python", "Election_Analysis", "analysis", "election_results.txt")` accordingly. 

Let's pretend that the Senate Primary Election CSV file has three rows of headers at the top of the file, providing information on the varios methods in which balots were cast for the election, and then starting at row 4, the CSV bigins listing off a few million of votes. (_In the origional CSV file, there was only one header row._) The base form of the script uses the line `header = next(reader)` to avoid counting the singular header row in the vote total calculation, in this Senate Primary Election CSV hypothetical (_containing three header rows_) we could write: 
````
    # Read three rows of headers
    header1 = next(reader)
    header2 = next(reader)
    header3 = next(reader)
````
This code would effectively read through all three rows of headers, such that we would not have to adjust the source CSV file, and then the script would continue counting up the remaining rows of votes with ease. Should another hypothetical CSV file have ZERO header rows, starting immediately with the voting data, we could remove all these lines entirely, as we would not need to insctruct the code to avoid tallying any lines.

Next, we must be aware of the fact that it is possible that the county names and candidate names might be stored in different columns as compared to our origional script. If, for instance candidate names were stored in the first column, and counties were stored in the 5th column, we'd need to adjust the following lines of code accordingly:

- `candidate_name = row[2]` becomes `candidate_name = row[0]`
- `county_name = row[1]` becomes `county_name = row[4]`

As long as there were no other drastic differences in this new Senate Primary Election CSV file, no other changes would be absolutely required in order to produce effective election audit results. Perhaps the new code could be adjusted further stylistically to specify which election's results are being calculated. Or, in the event that this code were to be used on a different scale, in which the term county would no longer be appropriate, we could easily adjust that change to be reflected in the output as well. 

With these stylistic changes, and after having adjusted the code to reflect any CSV format differentials, as discussed above, the script is capable of analysiing any future election, regardless of the number of candidates running for election, and regardless of the number of counties involved in casting votes. And for those reasons, this python script is quite valuable.
