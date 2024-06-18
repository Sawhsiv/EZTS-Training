x=[2,3,2,6,1,4,8,1]
for j in range(len(x)):
    for i in range(len(x)-1):
        if x[i]<x[i+1]:
            temp=x[i]
            x[i]=x[i+1]
            x[i+1]=temp
    print(x)           