import sqlite3
import re

def init_table_with_processed_data(cur):
    cur.execute("DROP TABLE IF EXISTS Numbers")
    return cur.execute('''
        CREATE TABLE IF NOT EXISTS Numbers (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            number TEXT
        )
    ''')

def get_total_number_of_responses(cur):
    cur.execute("SELECT COUNT(response) FROM Responses")
    return cur.fetchone()[0]

def clean_raw_data(response):
    # Eliminate commas from everywhere
    response = response.replace(",", "")
    # Eliminate trailing dots everywhere
    response = re.sub("(\.)$", "", response)
    # Transform twelve to from text to number 12
    response = re.sub("^twelve$", "12", response)
    return response

def extract_target_data(response):
    return re.findall(r'\d+\.?\d*', response)[0]

def validate_data(response):
    # If everything was correct it should be possible
    # to convert each string to interger or float
    # In case it fails, data needs further inspection and cleaning
    try: 
        response = int(response)
    except:
        response = round(float(response), 2)
    # Convert back to string
    return str(response)
    
def process_raw_data():
    # Establish connection to handle the clean data DB 
    conn_1 = sqlite3.connect('./data/numbersdb.sqlite')
    cur_1 = conn_1.cursor()
    # DELETEs and recreate the table for the number
    init_table_with_processed_data(cur_1)
    # Establish connection to the raw data DB
    conn_2 = sqlite3.connect('./data/rawdb.sqlite')
    cur_2 = conn_2.cursor()

    n_responses = get_total_number_of_responses(cur_2)
    if n_responses < 1:
        print("There are no numbers to clean.")
    else:
        cur_2.execute("SELECT response FROM Responses")
        for i in range(n_responses):
            raw_response = cur_2.fetchone()[0]
            clean_response = clean_raw_data(raw_response)
            number = extract_target_data(clean_response)
            number = validate_data(number)
            # if this doesn't blow everything is fine
            print(number)
            # Insert number to DB and commit changes
            cur_1.execute('INSERT INTO Numbers (number) VALUES ( ? )', ( number, ))

        print("There were " + str(n_responses) + " numbers that got process.\n")
        conn_1.commit()
        conn_1.close()
        conn_2.close()
    return True
