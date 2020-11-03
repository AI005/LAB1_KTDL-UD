import csv
import statistics
from random import choice
from collections import Counter
import os
from math import sqrt
from list_temp import *


def mean(list_data):
    return sum(list_data)/len(list_data)


def median(list_data):
    data = sorted(list_data)
    n = len(list_data)
    if n % 2 == 1:
        return list_data[n//2]
    else:
        i = n//2
        return (list_data[i - 1] + list_data[i])/2

def mode(list_data):
    result = list_data[0]
    for d in list_data:
        if list_data.count(d) > list_data.count(result):
            result = d
    return result

def stdev(list_data):
    mu = mean(list_data)
    return sqrt(sum([(point-mu)**2 for point in list_data])/len(list_data))


class Pandakungfu:
    #dataframe is a list of dict
    #format: [{'col1': val1, 'col2': val2, ...},
    #           ...
    #          {col1': valn-1, 'col2': valn, ...}]
    def __init__(self, filename):
        inputfile = open(filename, 'r')
        self.dataframe = list(self.read_csv(inputfile))
    
    def get_list_col_name(self):
        return [key for key in self.dataframe[0].keys()]

    #return name_col of row that missing value
    #ex: [[col1, col2], 
    #       [], 
    #     [col3]]
    #mean: row0 missing value of col1,col2
    #      row1 has no missing value
    #      row3 missing value of col3   
    def get_list_missing_data(self):
        return [[key for key, value in row.items() if value == ''] for row in self.dataframe]


    def display_list_missing_data(self):
        list_missing_data = self.get_list_missing_data()
        for index, keys in enumerate(list_missing_data):
            if len(keys) != 0:
                print('Hang ' + str(index) + ' thieu du lieu cua cac cot ' + str(keys))


    # Chuc nang 1: return name_col missing value
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
        return len(list_missing_data) - list_missing_data.count([])

    #Read file csv as list of Dict
    @staticmethod
    def read_csv(input_file):
        input_file.seek(0)
        csv_reader = csv.DictReader(input_file)
        for row in csv_reader:
            yield row
    
    #Write file csv from list of Dict
    def write_csv(self, filename):
        with open(filename, 'w') as file:
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
            return mean([float(x) for x in self[col_name] if x != ''])
        except:
            print("type's" + col_name + "is not numeric"+ col_name + ' has no value')


    def get_median(self, col_name):
        try:
            return median([float(x) for x in self[col_name] if x != ''])
        except:
            print("type's" + col_name + " is not numeric or " + col_name + ' has no value')


    def get_mode(self, col_name):
        return mode([x for x in self[col_name] if x != ''])


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


    #return set(min, max)
    def get_min_max(self, col_name):
        if self.is_numeric(col_name):
            return (min([float(x) for x in self[col_name] if x != '']), 
                    max([float(x) for x in self[col_name] if x != '']))
        else:
            raise Exception("cannot get minmax of non-numeric")
        
        
    def normalize_by_minmax(self, col_name, new_min = 0, new_max = 1):
        if new_min >= new_max:
            raise Exception('erorr: new_min >= new_max')
        
        _min, _max = self.get_min_max(col_name)
        new_col = list(map(lambda a: a if a == '' else str((float(a) - _min)*(new_max - new_min)/(_max - _min) + new_min),
                       self[col_name]))
        
        self.replace_col(col_name, new_col)
        
        
    def get_stdev(self, col_name):
        try:
            return stdev([float(x) for x in self[col_name] if x != ''])
        except:
            print("type's" + col_name + "is not numeric")
    
    
    def normalize_by_zcore(self, col_name):
        stdev = self.get_stdev(col_name)
        mean = self.get_mean(col_name)
        new_col = list(map(lambda a: a if a == '' else str((float(a) - mean)/stdev), self[col_name]))
        self.replace_col(col_name, new_col)
    
    
    def append_col(self, new_col, new_col_name):
        for i in range(len(self.dataframe)):
            self.dataframe[i][new_col_name] = new_col[i]

   
   
    #ex: 'colname1'*'colname2' => colname1*colname2 => list_temp(self[colname1])*list_temp(self[colname2]) => call eval 
    def calculate_express(self, express, new_col_name):
        #remove charater ' in express
        count = express.count("'")
        express = express.replace("'", "", count)
        
        count = express.count("[")
        express = express.replace("[", "(", count)
        
        count = express.count("]")
        express = express.replace("]", ")", count)
        
        list_col_name = self.get_list_col_name()
        for a in list_col_name:
            if a in express:
                rep = 'list_temp(self["' + a + '"])'
                express = express.replace(a, 'list_temp(self["' + a + '"])')
        
        new_col = eval(express)
        self.append_col(new_col.get_data(), new_col_name)