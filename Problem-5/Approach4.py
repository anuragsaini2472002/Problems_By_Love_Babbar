''' 
Move all negative numbers to beginning and positive 
to end 

##  Using Extra space

'''

'''
Input = -12,11,-13,-5,6,-7,5,-3,-6
Output = -12,-13,-4,-7,-3,-6,11,6,5
Order is not important
'''

def arrange(arr,n):
    l = []
    for i in range(0,n):
        if(arr[i]<0):
            l.insert(0,arr[i])
        elif(arr[i]>0):
            l.append(arr[i])
    print(f"Sorted array: {l}")    

arr = [-12,11,-13,-5,6,-7,5,-3,-6]
n = len(arr)
result = arrange(arr,n)
