monthlyExpense=[2200,2350,2600,2130,2190]
month=['January','February','March','April','May']
def printExpense(inde):
    for i in range(inde):
        print(month[i],'=',monthlyExpense[i])
def diffExpense(x,y):
    diff=monthlyExpense[x]-monthlyExpense[y]
    return diff
def quartExpense():
    sum=0
    for i in range(3):    
        sum=sum+monthlyExpense[i]
    return sum
def checkExpense():
    for i in range(5):
        if monthlyExpense[i]==2000:
            print('It matches.')
            break
        else:
            print('Not Matches.')
            break
def correctExpense(ind,redu):
    monthlyExpense.insert(ind,monthlyExpense[ind]-redu)


printExpense(5)
print('The Difference between expenses between January and February:',abs(diffExpense(0,1)))
print('The Total Expense For the First Quarter:',quartExpense())
checkExpense()
month.append('June')
monthlyExpense.append(1980)
printExpense(len(monthlyExpense))
correctExpense(3,200)
print(len(monthlyExpense))
printExpense(6)
