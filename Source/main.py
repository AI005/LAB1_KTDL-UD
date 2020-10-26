import csv


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


filename = 'house-prices.csv'
with open(filename) as file:
    spamreader = csv.DictReader(file)
    list_missing_data = get_list_missing_data(spamreader)
    display_list_missing_data(list_missing_data)


    #Chuc nang 1
    print('Cac cot cua ')
    print('Cac cot bi thieu du lieu: ' + str(list_col_less_data(list_missing_data)))
    print('So dong bi thieu du lieu: ' + str(get_number_of_row_less_data(list_missing_data)))


