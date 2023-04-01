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
- [ChatGPT, Numbers and The Meaning of Life!](https://jzstats.github.io/chatgpt-numbers-and-the-meaning-of-life/)


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

### Usage

You can either use the program to reproduce my results
or to reproduce the experiment with new data. It's up to you!

First download the files with the command:

> git clone https://github.com/jzstats/chatgpt-numbers-and-the-meaning-of-life

and cd into the repo.

#### Requirements

It is required to have a valid api key that can be used to 
communicate with the ChatGPT's API. 

Create a file called 'config.py',
and put a line:  
> api_key = \<the-api-key-of-the-user\\>

This file will be sourced by 'main.py' when 
it tries to retrieve the raw data.

(it was not included in the repo 
to hide the API key used for the project, 
which is my personal one!)

#### Reproduce my Results

In order to reproduce my results run the 'main.py' script. 

When it asks for the number of desired observations, 
input 0 and you are practically done! 

Next you can explore the top n results
and may compare them with mine.

Finally to produce the wordcloud, 
run the script 'visuallize_results.py' 
and open in a the browser the file 'wordcloud.htm'

#### Reproduce the Experiment

If you wish to reproduce the same experiment but with new data 
you should first delete the 'data/rawdb.sqlite' DB.

Then run the script 'main.py'.

When it asks for the number of desired observations, 
input the number of observations you want to collect. 
The data retrieving process is quit slow 
and may take from minutes to hours depending on the sample.

THINGS MAY BREAK in the data processing step,
as the cleaning and extraction is sensitive to the data 
I had collected and it is possible that you may need to modify
the script 'process_the_raw_data.py' to fit your observations.

Then you can explore your results and may compare them with mine.

Finally to produce the wordcloud, 
run the script 'visuallize_results.py' 
and open in a the browser the file 'wordcloud.htm'

<br> 

### Disclaimer

The scripts and files used for the visualization,
were taken almost as is from contents of the courses 
and specifically correspond to the files:  

1. 'visualize_results.py' to 'code3/gmane/gword.py'
2. 'wordcloud.js' to 'code3/gmane/gword.js'
3. 'wordcloud.htm' to 'code3/gmane/gword.htm'

And the JavaScript Libraries as is: 
1. d3.v2.js
2. d3.layout.cloud.js

from the repo:
> https://github.com/csev/py4e

<br>

### FAQ

#### Why the data retrieving process hangs for a minute evry 20 or 30 requests?

Intentionally, to conform with what the openai's API demands.

