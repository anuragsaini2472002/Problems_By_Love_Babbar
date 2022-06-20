# Find the Kth smallest element using While loop
# O(n)

arr = [7,10,4,3,20,15]
i = 0
j = len(arr)
minVal = arr[0]
while(i<j):
    if arr[i]<minVal:
        minVal = arr[i]
    i += 1

print(f"Min: {minVal}")
