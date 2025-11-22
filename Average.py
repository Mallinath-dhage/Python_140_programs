# WAP to input 2 floating point numbers & print their average.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
average = (num1 + num2) / 2
print(f"The average of", {num1}, "and", {num2}, "is:", {average})

# Here we are taking two floating point numbers as input from the user using the input() function and converting them to float type.
# We then calculate their average using the formula (num1 + num2) / 2 and store it in the variable 'average'.
# Finally, we print the result using an f-string to format the output. 