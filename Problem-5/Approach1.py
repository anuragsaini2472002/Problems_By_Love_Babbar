''' 
Move all negative numbers to beginning and positive 
to end with constant extra space
'''

'''
Input = -12,11,-13,-5,6,-7,5,-3,-6
Output = -12,-13,-4,-7,-3,-6,11,6,5
Order is not important
'''
def arrange(arr,n):
    j = 0
    for i in range(0,n):
        if(arr[i]<0):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            j = j+1
    print(arr)


arr = [-12,11,-13,-5,6,-7,5,-3,-6]
n = len(arr)
arrange(arr,n)