# WAP to check if a number is a multiple of 7 or not.

num = int(input("Enter any random number:"))
if(num % 7 == 0):
    print(f"Given number",{num},"is multiple of 7.")
else:
    print("Try again!!, With different number.")

"""
Here in this program, we are taking an integer input from the user and checking if it is a multiple of 7 by using the modulus operator (%).
If the remainder when the number is divided by 7 is zero, it means the number is a multiple of 7.
If the condition is true, we print that the number is a multiple of 7; otherwise, we prompt the user to try again with a different number.
This program effectively demonstrates the use of conditional statements and arithmetic operations in Python.
"""