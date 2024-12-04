class rectangle:
    def __init__(self,c,l,w):
        self.color=c
        self.length=l
        self.width=w
    def area(self):
        self.area=self.length*self.width
        return self.area
    def per(self):
        self.per=2*(self.length+self.width)
        return self.per
    def diagonal(self):
        self.diagonal=(self.length**2 + self.width**2)**(1/2)
        return self.diagonal

myRect1=rectangle('red',4,2)
print('Color of Rectangle1=',myRect1.color)
print('Lenth of Rectangle=',myRect1.length)
print('Width of Rectangle=',myRect1.width)
print('Area of Rectangle is:',myRect1.area())
print('Perimeter of the Rectangle:',myRect1.per())
print('Diagonal of the Rectangle is:',myRect1.diagonal())