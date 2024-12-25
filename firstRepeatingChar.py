
def firstrepeatingchar(arr):

    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] == arr[j]:
                return arr[i]
arr = [10, 5, 3, 4, 3, 5, 6]
result1 = firstrepeatingchar(arr)
print(result1)

            