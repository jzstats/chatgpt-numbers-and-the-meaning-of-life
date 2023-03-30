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

def get_total_number_of_entries():
    conn = sqlite3.connect('./data/numbersdb.sqlite')
    cur = conn.cursor()
    cur.execute("SELECT COUNT(number) FROM Numbers")
    n = cur.fetchone()[0]
    conn.close()
    return int(n)

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

def input_getter():
    while True:
        try: 
            n = input("How many top results to show? (q to quit) ")
        except KeyboardInterrupt:
            print('\nUser Interrupt.')
            exit()
        if n == 'q' : exit()
        try:
            n = int(n)
        except:
            print('Unexpected input. Try again.')
            continue
        if n < 1: 
            print('..invalid input. Give a non-negatige number.')
            continue
        else:
            break
    return n

def present_summary(summary):
    top_n = input_getter()
    n = get_total_number_of_entries()
    print("Out of " + str(n) + " numbers: ")
    aggr_perc = 0
    for k, v in summary.items():
        if top_n < 0: break
        top_n = top_n - 1
        perc = round(float(v)/n*100, 2)
        aggr_perc = aggr_perc + perc
        print(str(k) + " occured " + str(perc) + "% of times")

    print('\n' + 'Aggregated the  numbers cover ' + str(round(aggr_perc,2)) + '% of all observations.')
    return aggr_perc


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
