#Program to check the given number is Armstrong number is not 

num = int(input ("Enter a number:"))

nd = len(str(num))
temp = num
if temp <= 0:
    print("Only positive numbers allowed")

sum = 0
while temp > 0:
    d = temp % 10
    sum += d**nd
    temp //= 10

if sum == num:
    print(f"Given number", {num}, "is an Armstrong number.")
else:
    print(f"Given number", {num}, "is not an Armstrong number.")

#In line 5, converted the number to string to find the length of the number which is used as power while calculating the sum of digits raised to the power of number of digits.
#In line 12, calculated the number of digits only for positive numbers. using the modular operator to extract each digit and raising it to the power of number of digits and adding it to sum.
#In line 13, Calculated the sum of each digit raised to the power of number of digits.
#In line 14, removed the last digit from the number by performing integer floor division by 10.
#In line 16-20, compared the calculated sum with the original number to determine if it is an Armstrong number or not and printed the result.
#The program handles only positive integers as input.




# WAP to find the armstrong number in given range of numbers

lower = int(input ("Enter first number:"))
upper = int(input ("Enter second number:"))
for num in range(lower, upper + 1):
    nu = len(str(num))
    temp = num
    sum = 0

    while temp > 0:
        d = temp % 10
        sum += d**nu
        temp //= 10

    #if sum == num:
    print(sum)