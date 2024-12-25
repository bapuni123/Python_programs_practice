num = int(input("Enter a number:"))

s = num
sum = 0
while num!=0:
    r = num%10
    sum+=r**3
    num = num//10
if sum==s:
    print("The given number is an armstrong number")
else:
    print("The given number is not an armstrong number")