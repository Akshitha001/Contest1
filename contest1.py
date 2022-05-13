# This is a sample Python script.


a=int(input("Enter the range:"))
b=[]
c=[]
y=[]
for x in range(0,a):
    z=int(input('enter no'))
    if z >= 0:
        b.append(z)
    else :
        c.append(z)
y=b+c
print(y)



