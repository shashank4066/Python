arr=[int(i) for i in input().split()]
arr.sort()
min=0
max=0
for x in range(0,4):
    min+=arr[x]
print(min,end=" ")
for y in range(1,5):
    max+=arr[y]
print(max)