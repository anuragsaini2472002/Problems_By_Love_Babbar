# Using while loop

arr = [1000,11,445,1,330,3000]
i = 0
j = len(arr)
maxVal = arr[0]
minVal = arr[0]
while i < j:
    if arr[i] > maxVal:
        maxVal = arr[i]
    elif arr[i] < minVal:
        minVal = arr[i]
    i += 1


print(f"Max: {maxVal}, Min: {minVal}")
