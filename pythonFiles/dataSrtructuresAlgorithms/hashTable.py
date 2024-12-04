class hashTable:
    def __init__(self):
        self.Max = 10
        self.arr = [[] for i in range(self.Max)]
        
    def get_hash(self,key):
        h=0
        for char in key:
            h += ord(char)
            return h % self.Max
        
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        # self.arr[h] = val
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                self.arr[h][idx] = (key,val)
                found = True
                break
        if not found:
             self.arr[h].append((key,val))
            

    def __getitem__(self,key):
        h = self.get_hash(key)
        # return self.arr[h]
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
    
    def __delitem__(self,key):
         h = self.get_hash(key)
        #  self.arr[h] = None
         for index, element in enumerate(self.arr[h]):
             if element[0] == key:
                 del self.arr[h][index]
        
if __name__ == '__main__':

        t = hashTable()
        t["march 6"] = 120
        t["march 8"] = 67
        t["march 9"] = 4
        t["march 17"] = 459
        
        print(t['march 6'])
        print(t.arr)
        del t["march 17"]
        print(t.arr)
        

