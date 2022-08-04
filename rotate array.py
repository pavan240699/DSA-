arr=[1,2,3,4,5]
temp=arr[-1]
for i in range(1,len(arr)):
    print(len(arr)-i)
    arr[len(arr)-i] = arr[len(arr)-i - 1]
arr[0]=temp
print(arr)
