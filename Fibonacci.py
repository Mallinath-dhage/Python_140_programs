#WAP to print the Fibonacci series
#n = int(input("Enter the number of terms: "))
#a, b = 0, 1
#for i in range(n):
#    print(a, end=" ")
#    a, b = b, a + b

# --- IGNORE ---
#In line 2, took input from the user for the number of terms in the Fibonacci series.
#In line 3, initialized the first two terms of the Fibonacci series.
#In line 4, used a for loop to iterate n times to generate the Fibonacci series.
#In line 5, printed the current term in the series.
#In line 6, updated the values of a and b to the next two terms in the series using tuple unpacking.



n = int(input("Enter the number of terms: "))
f1, f2, f3 = 0, 1, 0
print(f"{f1}, {f2}")
print("Fibonacci Series: " )
for i in range(2, n):
    f3 = f1 + f2
    print(f"{f3}")
    f1 = f2
    f2 = f3

# --- IGNORE ---
#In line 2, took input from the user for the number of terms in the Fibonacci series.
#In line 3, initialized the first three terms of the Fibonacci series.
#In line 4, printed the first two terms of the series.
#In line 5, used a for loop starting from 2 to n to generate the remaining terms of the Fibonacci series.
#In line 6, calculated the next term in the series by adding the previous two terms
#In line 7, printed the current term in the series.
#In line 8 and 9, updated the values of f1 and f2 to the next two terms in the series.
