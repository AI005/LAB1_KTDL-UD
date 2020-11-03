
class list_temp():
    def __init__(self, data):
        try:
            self.data = list(map(lambda x: x if x == '' else float(x), [x for x in data]))
        except:
            print('data is not numeric')
      
    def __add__(self, other):
        # return list_temp([x + y for x, y in zip(self.data, other.data)])
        result = []
        for a, b in zip(self.data, other.data):
            if isinstance(a, float) and isinstance(b, float):
                result.append(a + b)
            else:
                result.append('')
                
        return list_temp(result)
    
    def __sub__(self, other):
        result = []
        for a, b in zip(self.data, other.data):
            if isinstance(a, float) and isinstance(b, float):
                result.append(a - b)
            else:
                result.append('')
                
        return list_temp(result)
    
    def __div__(self, other):
        result = []
        for a, b in zip(self.data, other.data):
            if isinstance(a, float) and isinstance(b, float):
                result.append(a / b)
            else:
                result.append('')
                
        return list_temp(result)
    
    def __mul__(self, other):
        result = []
        for a, b in zip(self.data, other.data):
            if isinstance(a, float) and isinstance(b, float):
                result.append(a * b)
            else:
                result.append('')
                
        return list_temp(result)
    
    def get_data(self):
        return list(map(str, self.data))