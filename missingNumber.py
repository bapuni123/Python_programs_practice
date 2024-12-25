def findMissingNumber(arr,n):

    sum_arr = sum(arr)
   ## n = len(arr)
    sum_all_natural = n*(n+1)//2
    return sum_all_natural - sum_arr

n = 8
arr =  [1, 2, 4, 6, 3, 7, 8]

result = findMissingNumber(arr,n)
print(result)