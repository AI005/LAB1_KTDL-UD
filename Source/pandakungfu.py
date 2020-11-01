import csv
import statistics
from random import choice
from collections import Counter
filename = 'test.csv'
# Tra ve list cac key co gia tri rong theo index
# vi du:
# + list[0] = {row1, row2}, nghia la tai row1, row2 hang thu 0 mang gia tri rong
# + list[1] = {}, nghia la tai hang thu 1 khong co gia tri nao rong
import os

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
        return list_missing_data.count([])

    #Read file csv as list of Dict
    @staticmethod
    def read_csv(input_file):
        input_file.seek(0)
        csv_reader = csv.DictReader(input_file)
        for row in csv_reader:
            yield row
    
    #Write file csv from list of Dict
    def write_csv(self, filename):
        with open('new_test.csv', 'w') as file:
            writer = csv.DictWriter(file,fieldnames=self.get_list_col_name())
            writer.writeheader()
            writer.writerows(self.dataframe)

    # get list values of col = col_names
    def __getitem__(self, col_name): 
        return [row[col_name] for row in self.dataframe]


    def replace_col(self, col_name, new_col):
        for i in range(0, len(self.dataframe)):
            self.dataframe[i][col_name] = new_col[i]
    

    def get_mean(self, col_name):
        try:
            return statistics.mean([float(x) for x in self[col_name] if x != ''])
        except:
            print("type's" + col_name + "is not numeric")


    def get_median(self, col_name):
        try:
            return statistics.median_grouped([float(x) for x in self[col_name] if x != ''])
        except:
            print("type's" + col_name + "is not numeric")


    def get_mode(self, col_name):
        return choice(statistics.multimode([x for x in self[col_name] if x != '']))


    def fill_missing_value_of_col(self, col_name, type='mode'):
        if type == 'mean':
            value = str(self.get_mean(col_name))
        elif type == 'median':
            value = str(self.get_median(col_name))        
        elif type == 'mode':
            value = self.get_mode(col_name)
        else:
            raise Exception('missing argument-type')
        
        new_col = list(map(lambda a: a if a != '' else value, self[col_name]))
        self.replace_col(col_name, new_col)
    
    
    def is_numeric(self, col_name):
        return all(map(lambda a: True if a == '' or str.isnumeric(a) else False, self[col_name]))
            
                       
    # fill all missing value with mean, median, mode
    def fill_all_missing(self, type='mode'):
        list_name = self.get_list_col_less_data()
        for col_name in list_name:
            if self.is_numeric(col_name):
                self.fill_missing_value_of_col(col_name, type)
            else:
                self.fill_missing_value_of_col(col_name,type='mode')
            
    def __str__(self):
        string_output = '\n'.join(list(map(str, self.dataframe)))
        return string_output
    
        # width = 13
        # list_col_name = self.get_list_col_name()
        # header = 'print('
        # for a in list_col_name:
        #     header += "'|" + a + "'" ".ljust("+str(width) +")+"

        # header = header[0:-1]    
        # header += ")"
        # eval(header)

        # #Print data
        # for row in self.dataframe:
        #     cmd = 'print('
        #     for key, value in row.items():
        #         cmd += "'|" + value + "'" ".ljust("+ str(width) +")+"
        #     cmd = cmd[0:-1]
        #     cmd += ")"
        #     eval(cmd)
        # Get width, height of terminal
        # table = ""
        # width = 10
        # width_ter, height_ter = os.popen('stty size', 'r').read().split()
        # line = "     "
        # list_col_name = self.get_list_col_name()
        # line += "|".join([a.rjust(width) for a in list_col_name])
        # while true:
        #     if len(line) >= width_ter:
                
        
        
    def remove_row_by_percent_missing(self, percent=0.5):
        self.dataframe = list(filter(lambda row: Counter(row.values())['']/ len(row) <= percent, self.dataframe))[:]


    def remove_col_by_percent_missing(self, percent=0.5):
        list_col_remove = [col_name for col_name in self.get_list_col_name() 
                           if Counter(self[col_name])['']/len(self.dataframe) >= percent]

        for row in self.dataframe:
            for name_col in list_col_remove:
                del row[name_col]


    def remove_duplicate_row(self):
        self.dataframe = [dict(t) for t in {tuple(row.items()) for row in self.dataframe}]


    def get_min_max(self, col_name):
        pass
    
    def normalize_by_minmax(self, col_name, new_min = 0, new_max = 1):
        list_value_col = self[col_name]

        _min, _max = float(min(list_value_col, key=float)), float(max(list_value_col, key=float))
        self.replace_col(self.dataframe, col_name, 
                         [str((float(x) - _min)*(new_max - new_min)/(_max - _min) + new_min) 
                          for x in list_value_col])

    def normalize_by_zcore(table, name_col):
        pass