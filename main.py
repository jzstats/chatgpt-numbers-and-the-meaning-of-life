from retrieve_raw_data import retrieve_raw_data
from process_raw_data import process_raw_data
from summarize_results import summarize_results
#from visualize_results import visualize_results

# Collect Raw Data 
# as raw responses from ChatGPT agent.
# This process is restartable,
# meaning that any new request are added to the already existing ones
# in the 'rawdb.sqlite' DB
retrieve_raw_data()

# Process Raw Data
# to standarize response values and extract the numbers
# ATTENTION: Deletes the DB 'numbersdb.sqlite' if it exists
#            and recreates it from contents of 'rawdb.sqlite'
# process_raw_data()

# Summarize Results
summarize_results()

# Visualize Results
#visualize_results()


