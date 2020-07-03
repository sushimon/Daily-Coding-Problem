# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
def prod(array):
    length = len(array)
    l, r, ans = [0] * length, [0] * length, [0] * length
    
    l[0] = 1
    for i in range(1, length):
        l[i] = l[i -1] * array[i - 1]
    
    r[length - 1] = 1
    for i in range(length - 2, -1, -1):
        r[i] = r[i + 1] * array[i + 1] 
    
    for i in range(length):
        ans[i] = l[i] * r[i]
    
    return ans

print(prod([1, 2, 3, 4, 5]))
print(prod([3, 2, 1]))
