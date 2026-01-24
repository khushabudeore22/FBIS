# # While -loop question :-

# # Write a program to print numbers from 1 to 10 using a while loop.
# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# # Write a program to print numbers from 10 to 1 using a while loop.
# i = 10
# while i >= 1:
#     print(i)
#     i -= 1

# # Write a program to print all even numbers between 1 and 50 using a while loop.
# i = 2
# while i <= 50:
#     print(i)
#     i += 2

# # Write a program to print all odd numbers between 1 and 30 using a while loop.
# i = 1
# while i <= 30:
#     print(i)
#     i += 2

# # Write a program to find the sum of numbers from 1 to 100 using a while loop.
# i = 1
# total = 0
# while i <= 100:
#     total += i
#     i += 1
# print(total)

# # Write a program to print the multiplication table of a given number using a while loop.
# n = int(input("Enter number: "))
# i = 1
# while i <= 10:
#     print(n, "x", i, "=", n*i)
#     i += 1

# # Write a program to count the number of digits in a given number using a while loop.
# n = int(input("Enter number: "))
# count = 0
# while n > 0:
#     count += 1
#     n //= 10
# print(count)

# # Write a program to find the sum of digits of a number using a while loop.
# n = int(input("Enter number: "))
# total = 0
# while n > 0:
#     total += n % 10
#     n //= 10
# print(total)

# # Write a program to reverse a given number using a while loop.
# n = int(input("Enter number: "))
# rev = 0
# while n > 0:
#     rev = rev*10 + n%10
#     n //= 10
# print(rev)

# # Write a program to check whether a number is a palindrome using a while loop.
# n = int(input("Enter number: "))
# temp = n
# rev = 0
# while n > 0:
#     rev = rev*10 + n%10
#     n //= 10

# if temp == rev:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# num = int(input("Enter a number: "))
num=int(input("Enter a number: "))
temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum = sum + (digit ** 3)
    temp = temp // 10

if sum == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")


# Write a program to find the factorial of a number using a while loop.
# Write a program to print Fibonacci series up to n terms using a while loop.
# Write a program to check whether a number is prime using a while loop.
# Write a program to print all prime numbers between 1 and 100 using a while loop.
# Write a program to find the largest digit in a given number using a while loop.
# Write a program to find the smallest digit in a given number using a while loop.
# Write a program to count even and odd digits in a number using a while loop.
# Write a program to convert a decimal number into binary using a while loop.
# Write a program that keeps accepting numbers until the user enters 0 using a while loop.
# Write a program to print each character of a string using a while loop.
# Write a program to count vowels in a string using a while loop.
# Write a program to reverse a string using a while loop.
# Write a program to check whether a string is a palindrome using a while loop.
# Write a program to count occurrences of a character in a string using a while loop.
# Write a program to find the length of a string without using len() using a while loop.
# Write a program to print all elements of a list using a while loop.
# Write a program to find the sum of elements in a list using a while loop.
# Write a program to find the maximum element in a list using a while loop.
# Write a program to find the minimum element in a list using a while loop.