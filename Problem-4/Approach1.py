# Sort an array of 0s, 1s and 2s

arr = [0,2,1,2,0]

start = 0
end = len(arr)-1

while(start<end):
    if arr[start]>arr[end]:
        arr[start], arr[end] = arr[end], arr[start]
    start += 1

print(arr)
