

class list_temp():
    def __init__(self, data):
        try:
            self.data = map(lambda x: 0 if x == '' else float(x) for x in data)
        except:
            print('data is not numeric')
      
    def __add__(self, other):
        return list_temp([x + y for x, y in zip(self.data, other.data)])
    
    def __sub__(self, other):
        return list_temp([x - y for x, y in zip(self.data, other.data)])
    
    def __div__(self, other):
        return list_temp([x / y for x, y in zip(self.data, other.data)])
    
    def __mul__(self, other):
        return list_temp([x * y for x, y in zip(self.data, other.data)])
    
    def get_data(self):
        return self.data.copy()
    