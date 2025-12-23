#Program to check the given number is Armstrong number is not 

num = int(input ("Enter a number:"))

nd = len(str(num))
temp = num
if temp <= 0:
    print("Only positive numbers allowed")

while temp > 0:
    d = temp % 10
    sum += d**nd
    temp //= 10

if sum == num:
    print(f"Given number", {num} "is an Armstrong number.")
else:
    print(f"Given number"  {num} "is not an Armstrong number.")