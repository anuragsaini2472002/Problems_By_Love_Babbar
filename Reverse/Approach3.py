# Approach third -- Using Swaping
arr1 = [1,2,3]
i = 0
j = len(arr1)-1
while(i<j):
    arr1[i],arr1[j] = arr1[j],arr1[i]
    i += 1
    j -= 1
print(f"Reversed array using While loop: {arr1}")