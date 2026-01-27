<!-- Loop Assignment :-

# Print numbers from 1 to 10 using a for loop.
num=0
for i in range(1,11):
    print(i, end=" ")

# Print all even numbers between 1 and 20.
num=0
for i in range(1,21):
    if i % 2 == 0:
        print(i , end=" ")

# Print all odd numbers from 1 to 15.
num=1
for i in range(1,21):
    if i % 2 != 0:
        print(i , end=" ")

# Count how many numbers are divisible by 3 between 1 and 50.
count = 0
for i in range(1, 51):
    if i % 3 == 0:
        count += 1
print(count)

# Find the sum of numbers from 1 to 10.
sum=0
for i in range(1,11):
    sum+=i
    print(sum)

# Print each character of a string on a new line.
name="Khushi"
for i in name:
    print(i)

# Count how many vowels are present in a given string.
name = "khushabu"
vowels = "aeiou"
count = 0
for ch in name:
    if ch in vowels:
        count += 1
print(count)

# Print only uppercase letters from a string.
name="Khushi Deore"
for i in name:
    if i.isupper():
        print(i, end=" ")

# 9) Reverse a string using a for loop.
name="khushi"
rev=""
for i in name:
    rev=i+rev
    print(rev)

# 10) Count digits and letters separately in a string.
s = "abc123"
letters = digits = 0
for ch in s:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1
print("Letters:", letters, "Digits:", digits)


# Find the largest number in a list.
lst = [3, 7, 2, 9]
largest = lst[0]
for i in lst:
    if i > largest:
        largest = i
print(largest)

# Find the smallest number in a list.
lst = [3, 7, 2, 9]
smallest = lst[0]
for i in lst:
    if i < smallest:
        smallest = i
print(smallest)

# Count how many even and odd numbers are in a list.
lst = [1, 2, 3, 4, 5]
even = odd = 0
for i in lst:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even:", even, "Odd:", odd)

# Print duplicate elements from a list.
lst = [1, 2, 3, 2, 4, 1]
duplicates = []
for i in lst:
    if lst.count(i) > 1 and i not in duplicates:
        duplicates.append(i)
print(duplicates)

# Count how many times a given number appears in a list.
lst = [1, 2, 2, 3, 2]
num = 2
count = 0
for i in lst:
    if i == num:
        count += 1
print(count)

# Print numbers greater than the average of a list.
lst = [10, 20, 30, 40]
avg = sum(lst) / len(lst)
for i in lst:
    if i > avg:
        print(i)

# Check whether a number is prime using a for loop.
n = int(input("Enter the number: 4"))
prime = True
for i in range(2, n):
    if n % i == 0:
        prime = False
        break
print(prime)

# Print prime numbers between 1 and 50.
for num in range(2, 51):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)

# Print a multiplication table of a given number.
n = 5
for i in range(1, 11):
    print(n, "x", i, "=", n*i)

# Find the factorial of a number using a for loop.
n = 5
fact = 1
for i in range(1, n+1):
    fact *= i
print(fact)

# Check whether a string is a palindrome.
s = "madam"
rev = ""
for ch in s:
    rev = ch + rev
print(s == rev)

# Count words in a sentence using a for loop.
s = "I love Python"
count = 1
for ch in s:
    if ch == " ":
        count += 1
print(count)

# Find the first repeated character in a string.
s = "programming"
seen = ""
for ch in s:
    if ch in seen:
        print(ch)
        break
    seen += ch

# Remove duplicate characters from a string.
s = "banana"
result = ""
for ch in s:
    if ch not in result:
        result += ch
print(result)

# Find the sum of digits of a number.
n = 123
total = 0
for d in str(n):
    total += int(d)
print(total)

# Check whether a number is an Armstrong number.
n = 153
total = 0
for d in str(n):
    total += int(d)**3
print(total == n)

# Print Fibonacci series up to n terms.
n = 5
a, b = 0, 1
for i in range(n):
    print(a)
    a, b = b, a + b

# Find the second largest number in a list.
lst = [10, 20, 30, 40]
lst.sort()
print(lst[-2])

# Print a pattern using * and a for loop.
for i in range(1, 6):
    print("*" * i)

# Separate positive and negative numbers from a list. -->
lst = [-1, 2, -3, 4]
positive = []
negative = []
for i in lst:
    if i >= 0:
        positive.append(i)
    else:
        negative.append(i)
print("Positive:", positive)
print("Negative:", negative)