cars = ('Audi','Mercedes','Mercedes','BMW')
print(cars)
#tuple with one item
car = ('Audi',)
print(car)
#length of tuple
print('length of cars=',len(cars))
#Creating tuple using tuple() Constructor
carss = (('Ferrari','Lamborgini','Roll Royce'))
print(carss)

#Accessing Tuple items

#accessing tuple items through +ve indexing
print(cars[1])
#accessing tuple items through -ve indexing
print(cars[-1],cars[-2])
#accessing tuple items through Slicing
print(cars[1:3])
print(cars[1:])
print(cars[:])

#Update a tuple

#adding items to a tuple(conver tuple to list then turn it back to tuple)
temp = list(cars)
temp.append('Toyota')
cars = tuple(temp)
print(cars)
#updating items of a tuple
temp = list(carss)
temp[1] = 'Toyota'
carss = tuple(temp)
print(carss)
#removing items of a tuple
temp = list(cars)
temp.remove('BMW')
cars = tuple(temp)
print(cars)
#remove entire tuple
del car

#Unpacking a tuple(packing-assingnig values to tuple, unpacking- extracting values of tuple)
car1, car2, car3, car4= cars
print(car1, car2, car3, car4)
#use of asterisk in unpacking tuple(used when no of variables are less than values of a tuple)
car1, *car2 = carss
print(car1, car2)

*car1, car2 = carss
print(car1, car2)



