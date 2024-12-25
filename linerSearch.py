res = [1,2,6,7,0,14,32,24,98,45]
x= int(input("Enter a number which you want to search: "))
temp =-1
for i in range(len(res)):
    if res[i] == x:
        temp = i
if temp > 0:
    print("the position of element in list is ", temp)
else:
    print("the element is not present in list")

