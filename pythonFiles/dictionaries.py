d = {'a':1,'b':2,'c':3,'d':4}
print(len(d))
e = dict([(1 ,'a'),(2 ,'b'),(3 ,'c'),(4 ,'d')])
print(len(e))
print(d['a'])
print(e[1])

print(d.get('a'))
print(d.get(1))

d_keys = d.keys()
d_values = d.values()
d_items = d.items()
print(d_keys)

d['e'] = 5
print(d)
print(d_keys)
print(d_values)
print(d_items)

#changin values using key names
d['a'] = 11
print(d_items)
#changing values using update() method
d.update({'a':22})
print(d_items)
#adding new items using update() method
d.update({'f':6})
print(d_items)

#Removing an item using pop() method

 #remove an item using key of method
print(d.pop('f'))
print(d_items)
 #remove item using popitem() method,removes last inserted item and returns tuple
print(d.popitem())
print(d_items)
 #remove an item using del keyword,using key of the item
del d['d']
print(d_items)
print(e)
del d
 #empty a dictionary using clear method
e.clear()
print(e)

#Copying a dictionary using assignment operator,changes made to copy will reflect on original dict
e = dict([(1 ,'a'),(2 ,'b'),(3 ,'c'),(4 ,'d')])
#copyying a dictionary using copy() method
e_copy = e.copy()
print(e_copy)
print(e)
e_copy[4] = 'e'
print(e_copy)
print(e)
#copying a dictionary using dict() method
d = {'a':1,'b':2,'c':3,'d':4}
d_copy = dict(d)
print(d_copy)

