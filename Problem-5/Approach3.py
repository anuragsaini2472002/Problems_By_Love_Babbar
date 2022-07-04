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
    i = 0
    j = n-1
    while(i<j):
        if(arr[i]<0):
            i+= 1
        elif(arr[j]>0):
            j-= 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
    print(arr)
   
arr = [-12,11,-13,-5,6,-7,5,-3,-6]
n = len(arr)
result = arrange(arr, n)