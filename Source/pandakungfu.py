import csv
import statistics
from random import choice
from collections import Counter
filename = 'test.csv'
# Tra ve list cac key co gia tri rong theo index
# vi du:
# + list[0] = {row1, row2}, nghia la tai row1, row2 hang thu 0 mang gia tri rong
# + list[1] = {}, nghia la tai hang thu 1 khong co gia tri nao rong

class Pandakungfu:
    
    def __init__(self, filename):
        inputfile = open(filename, 'r')
        self.dataframe = list(self.read_csv(inputfile))
    
         
    def get_list_col_name(self):
        return [key for key in self.dataframe[0].keys()]


    def get_list_missing_data(self):
        return [[key for key, value in row.items() if value == ''] for row in self.dataframe]


    def display_list_missing_data(self):
        list_missing_data = self.get_list_missing_data()
        for index, keys in enumerate(list_missing_data):
            if len(keys) != 0:
                print('Hang ' + str(index) + ' thieu du lieu cua cac cot ' + str(keys))


    # Chuc nang 1
    def get_list_col_less_data(self):
        list_missing_data = self.get_list_missing_data()
        result = set()
        for element in list_missing_data:
            for colname in element:
                result.add(colname)
        return result


    # Chuc nang 2
    def get_number_of_row_less_data(self):
        list_missing_data = self.get_list_missing_data()
        return len(list_missing_data)

    @staticmethod
    def read_csv(input_file):
        input_file.seek(0)
        csv_reader = csv.DictReader(input_file)
        for row in csv_reader:
            yield row


    # chuc nang 3 

    # get list values of col = col_names
    def __getitem__(self, col_name): 
        return [row[col_name] for row in self.dataframe]


    def replace_col(self, col_name, new_col):
        for i in range(0, len(self.dataframe)):
            self.dataframe[i][col_name] = new_col[i]
    


    def get_mean(self, col_name):
        return statistics.mean([float(x) for x in self[col_name] if x != ''])


    def get_median(self, col_name):
        return statistics.median_grouped([float(x) for x in self[col_name] if x != ''])


    def get_mode(self, col_name):
        return choice(statistics.multimode([float(x) for x in self[col_name] if x != '']))


    def set_col_with_mean(self, col_name):
        mean_value = str(self.get_mean(col_name))
        new_col = list(map(lambda a: a if a != '' else mean_value, self[col_name]))
        self.replace_col(col_name, new_col)


    def set_col_with_median(self, col_name): #this function is
        median_value = str(self.median(col_name))
        new_col = list(map(lambda a: a if a != '' else median_value, self[col_name]))
        self.replace_col(col_name, new_col)


    def get_full_col_with_mode(table, col_name):
        mode_value = str(self.get_mode(col_name))
        new_col = list(map(lambda a: a if a != '' else mode_value, self[col_name]))
        self.replace_col(col_name, new_col)


    def display(self):
        print(self.dataframe)
        width = 13
        list_col_name = self.get_list_col_name()
        header = 'print('
        for a in list_col_name:
            header += "'|" + a + "'" ".ljust("+str(width) +")+"

        header = header[0:-1]    
        header += ")"
        eval(header)

        #Print data
        for row in self.dataframe:
            cmd = 'print('
            for key, value in row.items():
                cmd += "'|" + value + "'" ".ljust("+ str(width) +")+"
            cmd = cmd[0:-1]
            cmd += ")"
            eval(cmd)


    def remove_row_by_percent_missing(percent = 0.5):
        self.dataframe = list(filter(lambda row: Counter(row.values())['']/ len(row) <= percent, self.dataframe))[:]


    def remove_col_by_percent_missing(percent = 0.5):
        list_col_remove = [col_name for col_name in self.get_list_col_name() 
                           if Counter(self[col_name])['']/len(self.dataframe) >= percent]

        for row in self.dataframe:
            for name_col in list_col_remove:
                del row[name_col]


    def remove_duplicate_row(self):
        return [dict(t) for t in {tuple(row.items()) for row in self.dataframe}]


    def normalize_by_minmax(self, col_name, new_min = 0, new_max = 1):
        list_value_col = self[col_name]

        _min, _max = float(min(list_value_col, key=float)), float(max(list_value_col, key=float))
        self.replace_col(self.dataframe, col_name, [str((float(x) - _min)*(new_max - new_min)/(_max - _min) + new_min)
                                             for x in list_value_col])


    def normalize_by_zcore(table, name_col):
        pass