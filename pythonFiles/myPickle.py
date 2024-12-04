import pickle
fruits=['orange','apple','banana']
x=3
y=23.3
grades=[99,34,56,77]
with open('myData.pkl','wb') as f:
    pickle.dump(fruits,f)
    pickle.dump(x,f)
    pickle.dump(y,f)
    pickle.dump(grades,f)
with open('myData.pkl','rb') as f1:
    a=pickle.load(f1)
    b=pickle.load(f1)
    c=pickle.load(f1)
    d=pickle.load(f1)
print(a)
print(b)
print(c)
print(d)