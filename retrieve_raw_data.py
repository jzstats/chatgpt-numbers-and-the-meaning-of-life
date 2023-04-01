import sqlite3
import openai

from time import sleep

# The API Key is expected to exist in a file,
# called 'config.py' (in the same directory as this script),
# and to contain a variable named api_key
# with the value of your API Key.
from config import api_key

def init_raw_data_table(cur):
    # Create a table in the SQL Database to store
    # raw_responses from the ChatGPT.
    return cur.execute('''
            CREATE TABLE IF NOT EXISTS Responses (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                response TEXT
            )
        ''')

def request_number():
    # Make a request to ChatGPT throught it's API 
    # asking for a number to get back it's response.
    openai.api_key = api_key
    api_response = openai.ChatCompletion.create(
                model = 'gpt-3.5-turbo',
                messages = [ 
                    { 'role' : 'system', 'content' : 'number'  },
                    { 'role' : 'user', 'content' : 'give a number'  },
                ]
            )
    return api_response.to_dict_recursive()['choices'][0]['message']['content']
    
def retrieve_data_point(cur):
    # A single data point gets collected and stored in the DB.
    raw_response = request_number()
    print(raw_response)
    cur.execute('INSERT INTO Responses (response) VALUES ( ? )', ( raw_response, ))
    return raw_response

def input_getter():
    while True:
        try: 
            n = input("How many data points to collect? ")
        except KeyboardInterrupt:
            print('\nUser Interrupt.')
            exit()
        try:
            n = int(n)
        except:
            print('Unexpected input. Try again.')
            continue
        if n < 0: 
            print('..invalid input. Give a non-negatige number.')
            continue
        else:
            break
    return n

def retrieve_raw_data():
    # Ask user for the size of the sample 
    n = input_getter()
    # Init Connection to SQLite DB
    conn = sqlite3.connect('./data/rawdb.sqlite')
    cur = conn.cursor()
    # Init Table with Raw Data (if does not exists)
    init_raw_data_table(cur)
    # Collect n data points
    for i in range(n):
        try:
            retrieve_data_point(cur)
        except KeyboardInterrupt:
            print('\nUser Interrupt.')
            exit()
        except:
            # When a request fails for any reason
            # the process hangs for a minute
            # Mainly this is to conform with the ChatGPT's API
            # that accepts either 20 or 30 request per minute
            sleep(60)
        conn.commit()
    # Close Connection to SQLite3
    conn.close()

