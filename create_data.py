import time
import sqlite3
import openai
import config

def get_api_key():
    # The API Key is expected to exist in a file,
    # called 'config.py' (in the same directory as this script),
    # and to contain a variable named api_key
    # with the value of your API Key.
    return config.api_key 

def init_raw_data_table(cur):
    # Create a table in the SQL Database to store
    # raw_responses from the ChatGPT.
    return cur.execute('''
            CREATE TABLE IF NOT EXISTS Responses (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                response TEXT
            )
        ''')

def ask_for_a_number():
    # Make a request to ChatGPT throught it's API 
    # asking for a number to get back it's response.
    openai.api_key = get_api_key()
    api_response = openai.ChatCompletion.create(
                model = 'gpt-3.5-turbo',
                messages = [ 
                    { 'role' : 'system', 'content' : 'number'  },
                    { 'role' : 'user', 'content' : 'give a number'  },
                ]
            )
    return api_response.to_dict_recursive()['choices'][0]['message']['content']
    
def collect_a_data_point(cur):
    # A single data point gets collected and stored in the DB.
    raw_response = ask_for_a_number()
    print(raw_response)
    cur.execute('INSERT INTO Responses (response) VALUES ( ? )', ( raw_response, ))
    return raw_response


def get_raw_data(n):
    # Init Connection to SQLite DB
    conn = sqlite3.connect('./data/rawdb.sqlite')
    cur = conn.cursor()
    # Init Table with Raw Data (if does not exists)
    init_raw_data_table(cur)
    # Collect n data points
    for i in range(n):
        try:
            collect_a_data_point(cur)
        except:
            time.sleep(60)
        conn.commit()
    # Close Connection to SQLite3
    conn.close()



get_raw_data(5)

