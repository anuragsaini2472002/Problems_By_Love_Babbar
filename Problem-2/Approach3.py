# Find the maximum and minimum element in an array

'''
arr = [1000,11,445,1,330,3000]
Output: Max: 3000
        Min: 1
'''

# Approach Using Linear Search

class search:
    def __init__(self):
        self.max = 0
        self.min = 0
    
def getMaxMin(arr,n):
        maxmin = search()

# If only one element in an array
        if n==1:
            maxmin.max = arr[0]
            maxmin.min = arr[0]

# if we have more than two element
        if arr[0]>arr[1]:
            maxmin.max = arr[0]
            maxmin.min = arr[1]
        else:
            maxmin.max = arr[1]
            maxmin.min = arr[0]
        
        for i in range(2,n):
            if arr[i]>maxmin.max:
                maxmin.max = arr[i]
            elif arr[i]<maxmin.min:
                maxmin.min = arr[i]
        return maxmin

       


if __name__ == "__main__":
    arr = [1000,11,445,1,330,3000]
    size = len(arr)
    maxmin = getMaxMin(arr,size)
    print(f"Maximum element of an array is: {maxmin.max}")
    print(f"Minimum element of an array is: {maxmin.min}")
