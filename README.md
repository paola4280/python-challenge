# python-challenge
PYBANK Folder:
Contains two more folders: Analysis and Resources. The main code is located under Analysis. The input and output files are in the Resources folder. The output file is in the form of a txt file called "result.txt."

The following steps were needed to be completed in order to finish this challenge:
Calculate the following:
- The total number of months included in the dataset
- The net total amount of "Profit/Losses" over the entire period
- The changes in "Profit/Losses" over the entire period, and then the average of those changes
- The greatest increase in profits (date and amount) over the entire period
- The greatest decrease in profits (date and amount) over the entire period

To solve this challenge, first I read the csv file by using the Python command and utilized functions like len(), sum(), next(), print(), among others to answer the questions. 
I also used loops and if statements for the logical aspect of the algorithm. 

For debugging, I used Xpert Learning Assistant and ChatGPT, mostly to calculate the greatest profit increase (date and amount), but it finally worked out. 
"dates.append(row[0])"
"if change > greatest_increase:
                greatest_increase = change
                greatest_increase_date = row[0]"

PYPOLL Folder:
Contains two more folders: Analysis and Resources. The main code is located under Analysis. The input and output files are in the Resources folder. The output file is in the form of a txt file called "result.txt."

The challenge needed to calculate the following:
- The total number of votes cast
- A complete list of candidates who received votes
- The percentage of votes each candidate won
- The total number of votes each candidate won
- The winner of the election based on popular vote

As for PyBank, I used the same tools learned in class, and some new ones were learned while debugging and researching how to code certain lines correctly.
A line of code used from ChatGPT was 
" if candidate not in vote_counts:  
      vote_counts[candidate] = 0
  vote_counts[candidate] += 1"
That code was to count the votes per candidate. This if statement worked really well.
Another line of code I got help with was "winner = max(vote_counts, key=vote_counts.get)". I did not include the key section to the max() function.
Additionally, I got help with "for candidate, votes in vote_counts.items():" from ChatGPT to print the candidates and their votes section. I was not sure how to make that for loop work and this way worked out great, plus I did not know how to use items().
