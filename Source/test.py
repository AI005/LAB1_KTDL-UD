from collections import Counter
from statistics import multimode

list_dict = [{'mssv': '18120507', 'ten': 'Cong Phu', 'gioitinh': 'Nam', 'lop': '18ctt4', 'sotien': '30'}, 
             {'mssv': '18120517', 'ten': 'Binh Phuong', 'gioitinh': 'Nam', 'lop': '18ctt4', 'sotien': '30'}, 
             {'mssv': '18120516', 'ten': 'Trong Phuong', 'gioitinh': '', 'lop': '18ctt4', 'sotien': ''}, 
             {'mssv': '18120514', 'ten': 'ThienPhuc', 'gioitinh': 'Nam', 'lop': '18ctt4', 'sotien': '50'},
             {'mssv': '18120517', 'ten': 'Binh Phuong', 'gioitinh': 'Nam', 'lop': '18ctt4', 'sotien': '30'}, 
             {'mssv': '18120513', 'ten': '', 'gioitinh': '', 'lop': '18ctt4', 'sotien': ''}, 
             {'mssv': '18120514', 'ten': 'ThienPhuc', 'gioitinh': 'Nam', 'lop': '18ctt4', 'sotien': '50'},
             {'mssv': '18120517', 'ten': 'Binh Phuong', 'gioitinh': 'Nam', 'lop': '18ctt4', 'sotien': '30'}, 
             {'mssv': '18120626', 'ten': 'Quang Truong', 'gioitinh': '', 'lop': '', 'sotien': ''}]
             
new_list = [dict(t) for t in {tuple(d.items()) for d in list_dict}]
print(new_list)           