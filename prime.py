# WAP to find the prime numbers

num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")
else:
    print("Number should be greater than 1")
# --- IGNORE ---
#In line 3, checked if the number is greater than 1 as prime numbers are greater than 1.
#In line 4, iterated from 2 to half of the number to check for factors.
#In line 5, checked if the number is divisible by any number in the range.
#In line 6, if a factor is found, printed that the number is not prime and exited the loop.
#In line 8, if no factors are found, printed that the number is prime.
#In line 10-11, handled the case for numbers less than or equal to 1, which are not prime numbers.
