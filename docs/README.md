# ChatGPT, Numbers and the Meaning of Life!  

What is the 'favorite' number of ChatGPT? 

This question is in the core of this project.

## Prologue

I was wondering what biases may be revealed by an exploration 
of the most frequently occuring numbers from ChatGPT agent, 
and indeed there are some strong ones in favor of certain numbers.

It is fine to jump directly to the 'Results'
or even (better!) to 'Nerd Mythology and Fun' 
if you are not interested in the technical details.

And may you find the result quite amusing too!

<br>

## Synopsis

10000 responses were collected from the ChatGPT's API.
In each iteration the agent was requested to 'give a number' 
and the raw responses were collected and stored in a database.

The raw data was then processed 
in order to extract the number from the response 
and the value got stored in another database.

Finally the results were summarized and visualized

<br>

## Process

### Retrieving the Raw Data

The script 'retrieve_raw_data.py' was used to collect the data.
When it runs, it asks the user for the number of raw responses that should be gathered.

To achieve it, it communicates with the ChatGPT through the available API.

It is required for the user to already have access to the API 
and to put his API key in a file called 'config.py' 
which will contain one line:
> api_key = <the-api-key-of-the-user>

(this file was not included in the repo 
to hide the API key used for the project, 
which is my personal one!)

At each iteration the raw response get's stored 
as-is in an SQL Lite DB (called 'rawdb.sqlite').

### Cleaning the Raw Data

The script 'prossess_raw_data.py' was used to collect the data.

#### Overview

The raw responses (that were gathered in the previous phase),
needed to be processed as the agent returned them in various non-standard formats.

The responses got cleaned and the number of each response was extracted
and got stored in another SQL Lite DB.

#### Details  

Most of the numbers were in a good format, 
meaning that they contained just a positive integer number.

Sometimes big integer numbers had a comma in the thousands,
which needed to get eliminated.

In many cases the number was followed by a single dot,
which needed to be ommitted.

Also very frequently the numbers were accompanied by some text 
from which they needed to got extracted.

In one case the number 12 was return as text, 'twelve',
which got converted to 

One response contained 3 numbers, from which only the first got counted as valid
and ectracted.

Only one floating point number occured, pi which was given in 
variations of decimal digits. It was decided to round it to 2 
so that all will correctly count as 3.14 for all cases.


#### Attension

The cleaning phase is not fully robust, as the process may fail 
if one uses the script 'retrieve_raw_data.py 'to collect new data. 

It is possible that there will be needed to manually 
inspect the data in order to identify and handle some unexpected anomalies 
that were not encountered in this project.

When the script runs it deletes the 'numbersdb.sqlite' DB 
and creates a new one from the 'rawdb.sqlite' DB. Care!
It is suggested to comment out the relevant line from 'main.py'
once you have the raw data processed.

### Summarizing the Results

The script 'summarize_results.py' was used to summarize the results.

# Overview

The results were summarized in order to identify those numbers 
that occurred more often as well as their frequency.

### Visuallizing the Results

The script 'visualize_results' was used to visuallize the results,
which takes into acount the occurances of each number 
and produces the normalized sizes of the numbers 
that got stored in the file 'wordcloud.js'.

Then the numbers get plotted in wordcloud,
using the file 'wordcloud.htm', 
that can be opened in the browser to 
visually examine the top 50 most frequently occuring numbers.

#### Disclaimer

These three scripts that were used for the visuallization, 
were taken almost as is from contents of the courses and correspond to the 

files:  
1. 

from the repo:
> https://github.com/...

<br>

## Results

The most frequently occuring, the top 5 and the top 50 numbers 
are presented along with their frequency from a sample of 10000 observations.

### ChatGPT's Favorite Number

ChatGPT's favorite number is... 42!! 
It was returned ... times out of the 10000 requests.

### Top 5 most frequently occuring numbers

The five most frequently occuring numbers were observed ...
out of a 10000 responses

Specifically


### Top 50 most frequently occuring numbers

The following figure displays the top 50 most frequently occuring numbers.
The size of each number is directly analogous 
to the relative frequency of each number. 

![image](./chatgpt_50_most_frequent_numbers.png)


## Nerd Mythology and Fun!

..42!! Really 42..

Although there is no doupt that the agent is of narrow intelligence, 
giving back this number is quite funny if one takes into account the 
classic novel 'Hitchkoc's Guide to the Galaxy' according to which..

.. SPOILER ALERT ..

.. 42 is The Meaning of Life! 

Isn't the irony quite apparent! 

Having a bot that is one step behind passing the 'Turing Test' 
giving this iconic number back in such frequency makes the imagination tick.
Does the bot hides something?? Is it some code for his fellow bots or a message for humanity?
For sure a decent 'Black Mirror' episode could be made out of this! 

<br>

## A Thank You to Vaggos!

My friend who knew and brought to my aweraness the story around 42.

## 










