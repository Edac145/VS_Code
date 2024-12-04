num=int(input('Enter the Number of grades:'))
x=[]
for i in range(0,num,1):
    grade=int(input('Enter Your Grade:'))
    x.append(grade)
for i in range(0,num,1):
    print(x[i])

sum=0
for i in range(0,num,1):
    sum=sum+x[i]

avg=sum/num
print('Average=',avg)


