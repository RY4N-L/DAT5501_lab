import pandas as pd
import matplotlib.pyplot as plt
# Load the CSV with semicolon delimiter
election_data_df = pd.read_csv('DAT5501_lab/Week-5/US-2016-primary.csv', delimiter=';')
election_data_df.fillna(0, inplace=True)  # Fill NaN values with 0
candidate = 'Donald Trump'

# Filter for one candidate, e.g. John Kasich
candidate_df = election_data_df[election_data_df['candidate'] == candidate]

# Find the total number of votes for the candidate
total_candidate_votes = candidate_df['votes'].sum()
#print(f'Total votes for {candidate}: {total_candidate_votes}')

# Find the total number of vote fraction in each state
state_vote_fractions = election_data_df.groupby('state')['fraction_votes'].sum() 
print(state_vote_fractions)

# Find the total number of votes in each state
state_total_votes = election_data_df.groupby('state')['votes'].sum()
#print(state_total_votes)

# Find the total number of votes for the candidate in each state
state_total_candidate_votes = candidate_df.groupby('state')['votes'].sum()
#print(state_total_candidate_votes)

# Find the fraction of votes for the candidate in each state
state_fractions = state_total_candidate_votes / state_total_votes
#print(state_fractions)

# Find the fraction of votes of each state compared to total votes for the candidate
candidate_vote_fractions = state_total_candidate_votes / total_candidate_votes

#sum candidate_vote_fractions should be 1
#print(candidate_vote_fractions)
#print(f"Total of vote fractions = {candidate_vote_fractions.sum()}")


# Plot histogram (bar chart for categorical states)
state_fractions_sorted = state_fractions.sort_values(ascending=False)
state_fractions_sorted.plot(kind='bar', title=f'Fraction of state votes for {candidate}', edgecolor='black')
plt.xlabel('State')
plt.ylabel('Total Fraction of Votes')
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot histogram of candidate vote fractions by state
candidate_vote_fractions_sorted = candidate_vote_fractions.sort_values(ascending=False)
candidate_vote_fractions_sorted.plot(kind='bar', title=f'Fraction of {candidate} Votes by State', edgecolor='black', color='orange')
plt.xlabel('State')
plt.ylabel('Fraction of Candidate Votes')
plt.grid(True)
plt.tight_layout()
plt.show()
