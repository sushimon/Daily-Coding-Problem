# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
def listAdd(lis, k):
    for x in range(len(lis)):
        for y in range(len(lis)):
            if lis[x] == lis[y]: continue
            else:
                if int(lis[x]) + int(lis[y]) == k:
                    return True
    return False

print(listAdd([10, 15, 3, 7], 17))
