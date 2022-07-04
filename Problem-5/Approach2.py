''' 
Move all negative numbers to beginning and positive 
to end with constant extra space
'''

'''
Input = -12,11,-13,-5,6,-7,5,-3,-6
Output = -12,-13,-4,-7,-3,-6,11,6,5
Order is not important
'''

def arrange(arr):
    arr.sort()
    print(arr)    

arr = [-12,11,-13,-5,6,-7,5,-3,-6]
result = arrange(arr)
