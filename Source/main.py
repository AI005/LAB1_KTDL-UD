import csv
import statistics
from random import choice

filename = 'test.csv'
# Tra ve list cac key co gia tri rong theo index
# vi du:
# + list[0] = {row1, row2}, nghia la tai row1, row2 hang thu 0 mang gia tri rong
# + list[1] = {}, nghia la tai hang thu 1 khong co gia tri nao rong      
def get_list_missing_data(table):
    return [[key for key, value in row.items() if value == ''] for row in table]


def display_list_missing_data(list_missing_data):
    for index, keys in enumerate(list_missing_data):    
        if len(keys) != 0:
            print('Hang ' + str(index) + ' thieu du lieu cua cac cot ' + str(keys))


#Chuc nang 1
def list_col_less_data(list_missing_data):
    result = set()
    for element in list_missing_data:
        for colname in element:
            result.add(colname)
    return result


#Chuc nang 2
def get_number_of_row_less_data(list_missing_data):
    return len(list_missing_data)

def read_the_csv(input_file):
    input_file.seek(0)
    csv_reader = csv.DictReader(input_file)
    for row in csv_reader:
        yield row


# chuc nang 3
def get_value_of_col(table, col_name):
    return [row[col_name] for row in table]

def mean(table, col_name):
    return statistics.mean([int(x) for x in get_value_of_col(table, col_name) if x != ''])

def median(table, col_name):
    return statistics.median_grouped([int(x) for x in get_value_of_col(table, col_name) if x != ''])

def mode(table, col_name):
    return choice(statistics.multimode([int(x) for x in get_value_of_col(table, col_name) if x != '']))

def get_full_col_with_mean(table, col_name):
    mean_value = str(mean(table, col_name))
    new_col = list(map(lambda a: a if a != '' else mean_value, get_value_of_col(table, col_name)))
    return new_col

def get_full_col_with_median(table, col_name):
    median_value = str(median(table, col_name))
    new_col = list(map(lambda a: a if a != '' else median_value, get_value_of_col(table, col_name)))
    return new_col

def get_full_col_with_mode(table, col_name):
    mode_value = str(mode(table, col_name))
    new_col = list(map(lambda a: a if a != '' else mode_value, get_value_of_col(table, col_name)))
    return new_col


with open(filename) as file:
    spamreader = read_the_csv(file)
    reader = list(spamreader)
    list_missing_data = get_list_missing_data(reader)

    # display_list_missing_data(list_missing_data)
    #Chuc nang 1
    print('Cac cot cua ')
    print('Cac cot bi thieu du lieu: ' + str(list_col_less_data(list_missing_data)))
    print('So dong bi thieu du lieu: ' + str(get_number_of_row_less_data(list_missing_data)))
    display_list_missing_data(list_missing_data)

    print(get_value_of_col(reader, col_name='sotien'))
    print(mean(reader, col_name='sotien'))
    print(median(reader, col_name='sotien'))
    print(mode(reader, col_name='sotien'))
    print(get_full_col_with_mean(reader, col_name='sotien'))
    print(get_full_col_with_median(reader, col_name='sotien'))
    print(get_full_col_with_mode(reader, col_name='sotien'))
