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
    
conn_1 = sqlite3.connect('./data/numbersdb.sqlite')
cur_1 = conn_1.cursor()

init_table_with_processed_data(cur_1)

conn_2 = sqlite3.connect('./data/rawdb.sqlite')
cur_2 = conn_2.cursor()

n_responses = get_total_number_of_responses(cur_2)
print(n_responses)
cur_2.execute("SELECT response FROM Responses")
for i in range(n_responses):
# for i in range(1000):
    response = cur_2.fetchone()[0]
    # Clean
    response = response.replace(",", "")
    response = re.sub("(\.)$", "", response)
    response = re.sub("^twelve$", "12", response)
    # Extract
    response = re.findall(r'\d+\.?\d*', response)[0]
    # Verify
    # if this doesn't blow everything is fine
    try: 
        response = int(response)
    except:
        response = round(float(response), 2)
    # Convert back to string
    response = str(response)
    print(response)
    # Insert number to DB and commit changes
    cur_1.execute('INSERT INTO Numbers (number) VALUES ( ? )', ( response, ))
    conn_1.commit()

conn_1.close()
conn_2.close()
