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
             

class A:
    def __init__(self,x = 'a',y = 'b'):
        self.a = x
        self.b = y
    
    def __getitem__(self,namecol):
        if namecol == 'a':
            return self.a
        if namecol == 'b':
            return self.b
        
        
    def __str__(self):
        return self.a + self.b
    def set(self,x,y):
        self.a = x
        self.b = y
        
    @staticmethod
    def create(x, y):
        return A(x,y)
    
    def copy(self):
        return A(self['1'],self['2'])
    
    
obj1 = A.create('1','2')
print(obj1)

