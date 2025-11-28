# WAP to find the greatest of 3 numbers entered by the user.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if (num1 >= num2) and (num1 >= num3):
    greatest = num1
elif (num2 >= num1) and (num2 >= num3):
    greatest = num2 
else:
    greatest = num3

print("Greatest of three numbers is: ", greatest)

"""
Here in this program, we are taking three integer inputs from the user and comparing them using conditional statements to determine the greatest number among them.
We use if-elif-else statements to compare the numbers and assign the greatest value to the variable 'greatest', which is then printed.
This program demonstrates the use of input handling, conditional statements, and comparison operators in Python.
The program ensures that all three numbers are compared correctly to find the maximum value.
The program also handles the case where two or more numbers are equal by using greater than or equal to (>=) in the comparisons.
This makes the program robust and reliable for various input scenarios.

"""
