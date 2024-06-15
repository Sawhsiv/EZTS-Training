l=[2,4,3,5,6,3,4,6,7,1,2,5]
sum = max = 0
k = int(input("Enter the no of continious digit: "))
print(len(l))
for i in range(0,len(l)-k+1):
    sum = 0
    for j in range(0,k):
        sum+=l[i+j]
    if max<sum:
        max = sum
        pos=i

print(max)
for j in range(0,k):
    print(l[pos+j])