l=[2,4,3,5,6,3,4,6,7,9,9,9]
window = max = 0
k = int(input("Enter the no of continious digit: "))

for j in range(0,k):
        window+=l[j]
l.append(0)
for i in range(0,len(l)-k):
    if max<window:
        max=window
        pos=i
    window = window+l[i+k]-l[i]

print("result")
print(max)
for j in range(0,k):
    print(l[pos+j])