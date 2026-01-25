# While -loop question :-

# Write a program to print numbers from 1 to 10 using a while loop.
i = 1
while i <= 10:
    print(i)
    i += 1

# Write a program to print numbers from 10 to 1 using a while loop.
i = 10
while i >= 1:
    print(i)
    i -= 1

# Write a program to print all even numbers between 1 and 50 using a while loop.
i = 2
while i <= 50:
    print(i)
    i += 2

# Write a program to print all odd numbers between 1 and 30 using a while loop.
i = 1
while i <= 30:
    print(i)
    i += 2

# Write a program to find the sum of numbers from 1 to 100 using a while loop.
i = 1
total = 0
while i <= 100:
    total += i
    i += 1
print(total)

# Write a program to print the multiplication table of a given number using a while loop.
n = int(input("Enter number: "))
i = 1
while i <= 10:
    print(n, "x", i, "=", n*i)
    i += 1

# Write a program to count the number of digits in a given number using a while loop.
n = int(input("Enter number: "))
count = 0
while n > 0:
    count += 1
    n //= 10
print(count)

# Write a program to find the sum of digits of a number using a while loop.
n = int(input("Enter number: "))
total = 0
while n > 0:
    total += n % 10
    n //= 10
print(total)

# Write a program to reverse a given number using a while loop.
n = int(input("Enter number: "))
rev = 0
while n > 0:
    rev = rev*10 + n%10
    n //= 10
print(rev)

# Write a program to check whether a number is a palindrome using a while loop.
n = int(input("Enter number: "))
temp = n
rev = 0
while n > 0:
    rev = rev*10 + n%10
    n //= 10

if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

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
n = int(input("Enter a number: "))
fact = 1
i = 1

while i <= n:
    fact = fact * i
    i += 1

print("Factorial:", fact)

# Write a program to print Fibonacci series up to n terms using a while loop.
n = int(input("Enter number of terms: "))
a, b = 0, 1
i = 1

while i <= n:
    print(a, end=" ")
    a, b = b, a + b
    i += 1

# Write a program to check whether a number is prime using a while loop.
n = int(input("Enter a number: "))
i = 2
flag = True

if n <= 1:
    flag = False

while i <= n // 2:
    if n % i == 0:
        flag = False
        break
    i += 1

if flag:
    print("Prime number")
else:
    print("Not a prime number")

# Write a program to print all prime numbers between 1 and 100 using a while loop.
num = 2

while num <= 100:
    i = 2
    prime = True

    while i <= num // 2:
        if num % i == 0:
            prime = False
            break
        i += 1

    if prime:
        print(num, end=" ")
    num += 1

# Write a program to find the largest digit in a given number using a while loop.
n = int(input("Enter a number: "))
largest = 0

while n > 0:
    digit = n % 10
    if digit > largest:
        largest = digit
    n //= 10

print("Largest digit:", largest)

# Write a program to find the smallest digit in a given number using a while loop.
n = int(input("Enter a number: "))
smallest = 9

while n > 0:
    digit = n % 10
    if digit < smallest:
        smallest = digit
    n //= 10

print("Smallest digit:", smallest)

# Write a program to count even and odd digits in a number using a while loop.
n = int(input("Enter a number: "))
even = 0
odd = 0

while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        even += 1
    else:
        odd += 1
    n //= 10

print("Even digits:", even)
print("Odd digits:", odd)

# Write a program to convert a decimal number into binary using a while loop.
n = int(input("Enter decimal number: "))
binary = ""

while n > 0:
    binary = str(n % 2) + binary
    n //= 2

print("Binary:", binary)

# Write a program that keeps accepting numbers until the user enters 0 using a while loop.
num = 1

while num != 0:
    num = int(input("Enter a number (0 to stop): "))

# Write a program to print each character of a string using a while loop.
s = input("Enter a string: ")
i = 0

while i < len(s):
    print(s[i])
    i += 1

# Write a program to count vowels in a string using a while loop.
s = input("Enter a string: ")
i = 0
count = 0

while i < len(s):
    if s[i].lower() in "aeiou":
        count += 1
    i += 1

print("Vowel count:", count)

# Write a program to reverse a string using a while loop.
s = input("Enter a string: ")
i = len(s) - 1
rev = ""

while i >= 0:
    rev += s[i]
    i -= 1

print("Reversed string:", rev)

# Write a program to check whether a string is a palindrome using a while loop.
s = input("Enter a string: ")
i = 0
j = len(s) - 1
flag = True

while i < j:
    if s[i] != s[j]:
        flag = False
        break
    i += 1
    j -= 1

if flag:
    print("Palindrome")
else:
    print("Not a palindrome")

# Write a program to count occurrences of a character in a string using a while loop.
s = input("Enter a string: ")
ch = input("Enter character to count: ")
i = 0
count = 0

while i < len(s):
    if s[i] == ch:
        count += 1
    i += 1

print("Occurrences:", count)

# Write a program to find the length of a string without using len() using a while loop.
s = input("Enter a string: ")
i = 0

while s[i:i+1] != "":
    i += 1

print("Length:", i)

# Write a program to print all elements of a list using a while loop.
lst = [10, 20, 30, 40]
i = 0

while i < len(lst):
    print(lst[i])
    i += 1

# Write a program to find the sum of elements in a list using a while loop.
lst = [10, 20, 30]
i = 0
total = 0

while i < len(lst):
    total += lst[i]
    i += 1

print("Sum:", total)

# Write a program to find the maximum element in a list using a while loop.
lst = [10, 50, 30, 40]
i = 0
max_val = lst[0]

while i < len(lst):
    if lst[i] > max_val:
        max_val = lst[i]
    i += 1

print("Maximum:", max_val)

# Write a program to find the minimum element in a list using a while loop.
lst = [10, 50, 30, 40]
i = 0
min_val = lst[0]

while i < len(lst):
    if lst[i] < min_val:
        min_val = lst[i]
    i += 1

print("Minimum:", min_val)