# WAP to find the occurrence of ‘$’ in a String
string_input = input("Enter a string: ")
count_dollar = string_input.count('$')  
print(f"The occurrence of '$' in the given string is: {count_dollar}")

# Here we are taking a string input from the user and then using the count() method to find the occurrence of the character '$' in that string.
# Finally, we are printing the result using an f-string to format the output.
# f-strings are a way to embed expressions inside string literals, using curly braces {}.