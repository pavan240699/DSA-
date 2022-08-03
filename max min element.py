arr=[5,4,5,6,8,1,4,2,2,8]
min=max=arr[0]
for i in arr:
    if i >= max:
        max=i
    if i <= min:
        min=i
print(min,max)