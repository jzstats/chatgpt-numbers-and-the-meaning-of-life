# ChatGPT, Numbers and the Meaning of Life!  

### Project  

**Question of Interest**
> *What is the 'favorite' number of ChatGPT?*

This was the target question that was examined in this project 
and the results were quite fun!

As expected, based on the data that was trained,
not all numbers are equally probable to occur! 

To the contrary out of a sample of 10000 numbers 
there are 5 that occured more than 50% of the time
and the most frequent of all them occured more than 20%.

So what is that number? Let me give you a hint:
Do you know about **The Meaning of Life**? 

If you want the full story, 
visit the project's GitHub Page:  

    - ChatGPT, Numbers and The Meaning of Life!  


<br> 

### About this repository

This repository was created to support 
the Honor's Track assignment of the Course:

> Capstone: Retrieving, Processing, and Visualizing Data with Python,
> from Python for Everybody Specialization
> by the University of Michigan, on Coursera

The course is taught by:

> Charles Russell Severance

The project was selected, designed and implemented 
according to the directions of the professor 
and in alignment with the spirit of the specialization. 

Specifically,
the target data source was identified, 
raw data was retrieved though an API,
then processed to get it clean
and the results were summarized and visualized.

Finally a GitHub Page was created to host and present the project.

<br>

### About the files contained in this repository

#### docs  
This directory contains all the files 
that were used in order to produce and populate
the project's GitHub Page.

#### \_\_pycache\_\_
W.I.P.

#### lib/python3.10/site-packages 
W.I.P.

#### pythonenv.cfg
W.I.P.
 
#### .gitignore
It was used to hide 'config.py' script,
which contains my API Key that was used 
to communicate with ChatGPT. 

#### config.py (not included in the repo)
This file contains one line with a variable named 'api_key' 
and the value of the API Key that was used in this project.
It gets imported by 'create_data.py' (which depends on it).
Was not included as it contains sensitive informotion,
but should be created if one tries to reproduce this project.

#### retrive_raw_data.py  
The script which was used to retrieve the raw data. 
It requests from ChatGPT agent through the API for a number, 
and stores the raw response in an SQL Lite DB, called 'rawdb.sqlite'.
Then repeats the process untill the specified number of responses is gathered.

#### rawdb.sqlite
An SQL Lite DB with one table which contains 
all the raw responses from ChatGPT agent,
without any processing.

#### process_raw_data.py
The script that was used to process the raw data.
It reads the table with raw data directly from the 'rawdb.sqlite',
and process one entry at a time in order to clean and extract 
the number from the raw response.
Then it stores the extracted number in another DB, 
called 'numbersdb.sqlite'.

#### numbersdb.sqlite
An SQL Lite DB with one table which contains 
all the prosseded clean data with the numbers 
returned from ChatGPT agent. 

#### summarize_results.py
This script was used to summarize the results.
It returns the top n more frequently occuring numbers 
and the times each of them occured.

#### visualize_results.py
This script is used to help produce the visualization of the results.
It normalizes sizes for each number 
in order to for them to appropriately get drawn
in the 'wordcloud' graph.

#### wordcloud.js
This file contains the normalized sizes
of the top 50 more frequently occuring numbers,
and was used by 'wordcloud.htm' file to produce
the wordcloud graph.

#### wordcloud.htm
This files produces a wordcloud of the top 50 
most frequently occuring numbers. 
It depends on the 'wordcloud.js' which contains 
the sizes that should be used to draw each number.



