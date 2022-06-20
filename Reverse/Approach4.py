# Using recursive method

def reverse(arr, start, end):
    if start >= end:
        return 
    arr[start], arr[end] = arr[end], arr[start] 
    reverse(arr, start+1, end-1)


arr = [1,2,3,4]
start = 0
end = len(arr)-1
reverse(arr,start, end)
print(f"Using recursive way: {arr}")