from collections import Counter
from statistics import multimode
import pandas as pd
import os
import csv
rows, columns = os.popen('stty size', 'r').read().split()
# print(rows, columns)
list_dict = [{'mssv': '18120507', 'ten': 'Cong Phu', 'gioitinh': 'Nam', 'lop': '18ctt4', 'sotien': '30'}, 
             {'mssv': '18120517', 'ten': 'Binh Phuong', 'gioitinh': 'Nam', 'lop': '18ctt4', 'sotien': '30'}, 
             {'mssv': '18120516', 'ten': 'Trong Phuong', 'gioitinh': '', 'lop': '18ctt4', 'sotien': ''}, 
             {'mssv': '18120514', 'ten': 'ThienPhuc', 'gioitinh': 'Nam', 'lop': '18ctt4', 'sotien': '50'},
             {'mssv': '18120517', 'ten': 'Binh Phuong', 'gioitinh': 'Nam', 'lop': '18ctt4', 'sotien': '30'}, 
             {'mssv': '18120513', 'ten': '', 'gioitinh': '', 'lop': '18ctt4', 'sotien': ''}, 
             {'mssv': '18120514', 'ten': 'ThienPhuc', 'gioitinh': 'Nam', 'lop': '18ctt4', 'sotien': '50'},
             {'mssv': '18120517', 'ten': 'Binh Phuong', 'gioitinh': 'Nam', 'lop': '18ctt4', 'sotien': '30'}, 
             {'mssv': '18120626', 'ten': 'Quang Truong', 'gioitinh': '', 'lop': '', 'sotien': ''}]
             
# with open('new_test.csv', ('w') as file:
#     writer = csv.DictWriter(file,fieldnames=['mssv','ten','gioitinh','lop','sotien'])
#     writer.writeheader()
#     writer.writerows(list_dict)
list_col_name = ['mssv', 'so tien', 'ten', 'lop']
s = "'so tien'*'mssv'+'so tien'"
#list_temp(self['so tien']*list_temp(self['mssv']))
for a in list_col_name:
    if a in s:
        rep = 'list_temp(slef["' + a + '"])'
        s = s.replace(a, 'list_temp(slef["' + a + '"])')
        
print(s)