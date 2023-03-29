import sqlite3

def data_getter():
    conn = sqlite3.connect('./data/numbersdb.sqlite')
    cur = conn.cursor()
    cur.execute("SELECT number FROM Numbers")

    numbers = list()
    while True:
        try: 
            number = cur.fetchone()[0]
        except: 
            break
        numbers.append(number)

    conn.close()

    return numbers

def count_number_occurances(numbers):
    counts = dict()
    for number in numbers:
        counts[number] = counts.get(number, 0) + 1
    return counts

def sort_counts_descending(counts):
    def value_getter(item):
        return item[1]
    sorted_counts = sorted(counts.items(), key = value_getter, reverse = True)
    return dict(sorted_counts)

def summarize_numbers(numbers):
    summary = count_number_occurances(numbers)
    summary = sort_counts_descending(summary)
    return summary

def get_top_n_input():
    while True:
        n = input("How many top results to show? ")
        try:
            n = int(n)
        except:
            continue
        if n < 1: 
            continue
        else:
            break
    return n

def present_summary(summary):
    top_n = get_top_n_input()
    for k, v in summary.items():
        if top_n == 0: break
        top_n = top_n - 1
        if v == 1:
            print(str(k) + " occured 1 time")
        else:
            print(str(k) + " occured " + str(v) + " times")


def summarize_results():
    while True:
        try: 
            # Read the Processed Data in python
            numbers = data_getter()

            # Summarize occurances of each number
            summary = summarize_numbers(numbers)

            # Present results 
            present_summary(summary)
        except KeyboardInterrupt:
            print('User Interrupt.')
            exit()
