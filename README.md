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

First download the files with the command

> git clone https://github.com/jzstats/chatgpt-numbers-and-the-meaning-of-life

and cd into the repo.

#### Reproduce my Results

In order to reproduce my results run the main.py file. 

When it asks for the number of desired observations, 
input 0 and you are practically done! 

Next you can explore the top n results (let's say the top 50).

Finally to produce the wordcloud, 
run the script 'visuallize_results.py' 
and open in a the browser the file 'wordcloud.htm'

Everything is expected to work smoothly, 
and you should get the exact same result as I had.

#### Reproduce the Experiment

If you wish to reproduce the same experiment but with new data 
you should first delete the 'data/rawdb.sqlite' DB.

Then run the script 'main.py'.

When it asks for the number of desired observations, 
input the number of observations you want to collect. 

THINGS MAY BREAK in the data processing step,
as the cleaning and extraction is sensitive to the data 
I had collected and it is possible that you may need to modify
the script 'process_the_raw_data.py' to fit your data.
It should not be that hard I think.. wish you luck!

Then you can explore your results.

Finally to produce the wordcloud, 
run the script 'visuallize_results.py' 
and open in a the browser the file 'wordcloud.htm'

### FAQ

#### Why the data retrieving process hangs for a minute evry 20 or 30 requests?

Intentianally, to conform with what the openai's API suggests.

