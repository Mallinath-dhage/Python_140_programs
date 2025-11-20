# WAP to input 2 int numbers, a and b. Print True if a is greater than or equal to b. If not print False
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
result = a >= b
print(f"Is", {a}, "greater than or equal to", {b},"?=", {result})

# Here we are taking two integer inputs from the user, a and b. 
# We then compare if a is greater than or equal to b using the >= operator, which returns a boolean value (True or False). 
# Finally, we print the result using an f-string to format the output.