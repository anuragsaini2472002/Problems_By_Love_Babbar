# Using For Loop
# Complexuty = O(n*n)

arr = [7,10,4,3,20,15]

for i in range(0, len(arr)-1):
    if arr[i+1]>arr[i]:
        minVal = arr[i]

print(minVal)

