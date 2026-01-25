# 1. Write a program to print all odd numbers from 1 to 50, but skip numbers divisible by 5 using `continue`.
for i in range(1, 51, 2):
    if i % 5 == 0:
        continue
    print(i)

# 2. Write a `for` loop that prints numbers from 1 to 100, but stops completely when a number divisible by both 7 and 9 is found.
for i in range(1, 101):
    if i % 7 == 0 and i % 9 == 0:
        break
    print(i)

# 3. Using a `while` loop, print numbers from 10 to 1, but skip number 6.
i = 10
while i >= 1:
    if i == 6:
        i -= 1
        continue
    print(i)
    i -= 1

# 4. Write a program to iterate through a list of names and stop printing once the name `"admin"` is found.
names = ["user", "guest", "admin", "test"]

for name in names:
    if name == "admin":
        break
    print(name)

# 5. Write a program to print the first 5 even numbers using a `while` loop.
count = 0
num = 2

while count < 5:
    print(num)
    num += 2
    count += 1

# 6. Write a loop that prints characters of a string, but does not print vowels.
s = input("Enter string: ")

for ch in s:
    if ch.lower() in "aeiou":
        continue
    print(ch)

# 7. Write a program using `for` loop and `else` to check whether a number exists in a list.
lst = [10, 20, 30, 40]
n = int(input("Enter number: "))

for i in lst:
    if i == n:
        print("Found")
        break
else:
    print("Not found")

# 8. Write a program that prints numbers from 1 to 20, but prints `"Skipped"` instead of the number 13.
for i in range(1, 21):
    if i == 13:
        print("Skipped")
    else:
        print(i)

# 9. Write a loop that prints numbers from 1 to 10, but uses `pass` for even numbers.
for i in range(1, 11):
    if i % 2 == 0:
        pass
    else:
        print(i)

# 10. Write a program that counts how many numbers between 1 and 100 are divisible by 3.
#count = 0
for i in range(1, 101):
    if i % 3 == 0:
        count += 1
print("Count:", count)

# 11. Write a program to find the first number between 1 and 1000 that is divisible by 11 and 13, then stop the loop.
for i in range(1, 1001):
    if i % 11 == 0 and i % 13 == 0:
        print(i)
        break

# 12. Write a program that prints all numbers from 1 to 100, but:
# Skip multiples of 3
# Stop if a number divisible by 17 appears
for i in range(1, 101):
    if i % 17 == 0:
        break
    if i % 3 == 0:
        continue
    print(i)

# 13. Using a `while` loop, keep taking numbers from the user until they enter 0, then print how many numbers were entered.
count = 0
while True:
    n = int(input("Enter number: "))
    if n == 0:
        break
    count += 1
print("Numbers entered:", count)

# 14. Write a program to check whether a given number is prime, using a loop and `break`.
n = int(input("Enter number: "))

for i in range(2, n):
    if n % i == 0:
        print("Not Prime")
        break
else:
    print("Prime")

# 15. Write a program that prints a triangle pattern using nested `for` loops.
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

# 16. Write a program to iterate through a list of integers and print **only the first negative number, then stop.
lst = [5, 10, -3, 7, -8]

for i in lst:
    if i < 0:
        print(i)
        break

# 17. Write a program using `for-else` to check if a number is present in a range from 1 to 50.
n = int(input("Enter number: "))

for i in range(1, 51):
    if i == n:
        print("Present")
        break
else:
    print("Not present")

# 18. Write a program that skips all numbers divisible by 4, but prints all others from 1 to 40.
for i in range(1, 41):
    if i % 4 == 0:
        continue
    print(i)

# 19. Write a program that finds the “sum of numbers until the sum becomes greater than 100”, then stops.
total = 0
i = 1

while True:
    total += i
    if total > 100:
        break
    i += 1

print("Sum:", total)

# 20. Write a program that prints numbers from 1 to 100, but replaces:

#  multiples of 3 → "Fizz"
#  multiples of 5 → "Buzz"
#  multiples of both → "FizzBuzz"
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# 21. Login Attempts System
#     A user gets 3 attempts to enter the correct password.
#     Stop the loop if the password is correct, otherwise block access.
password = "admin123"
attempts = 3

while attempts > 0:
    pwd = input("Enter password: ")
    if pwd == password:
        print("Login Successful")
        break
    attempts -= 1
else:
    print("Account Blocked")

# 22. ATM Withdrawal
#     Keep asking for withdrawal amount until the amount is less than or equal to balance.
balance = 5000

while True:
    amt = int(input("Enter withdrawal amount: "))
    if amt <= balance:
        print("Withdraw Successful")
        break
    print("Insufficient balance")

# 23. Student Attendance
#     Iterate through a student list and stop checking attendance when "absent" is found.
attendance = ["present", "present", "absent", "present"]

for status in attendance:
    if status == "absent":
        print("Absent found")
        break

# 24. Online Exam System
#     Skip a question if the student chooses "skip" and continue to the next question.
questions = ["Q1", "skip", "Q3"]

for q in questions:
    if q == "skip":
        continue
    print("Answering", q)

# 25. Inventory Check
#     Loop through product quantities and stop when **stock reaches zero**.
stock = [10, 8, 5, 0, 7]

for item in stock:
    if item == 0:
        print("Stock Empty")
        break

# 26. OTP Verification
#     Users have 5 chances to enter OTP. Stop immediately when OTP matches.
otp = "1234"
attempts = 5

while attempts > 0:
    entered = input("Enter OTP: ")
    if entered == otp:
        print("OTP Verified")
        break
    attempts -= 1

# 27. Website Visitor Counter
#     Count visitors until count reaches 100, then stop the loop.
count = 0

while count < 100:
    count += 1

print("Visitor limit reached")

# 28. Salary Processing
#     Skip employees whose salary is 0, process others.
salaries = [20000, 0, 30000, 0, 25000]

for sal in salaries:
    if sal == 0:
        continue
    print("Processed:", sal)

# 29. Menu-Driven Program
#     Show menu repeatedly until user selects `"Exit"`.
while True:
    choice = input("Enter choice (Exit to stop): ")
    if choice == "Exit":
        break

# 30. Game Lives System
#     The player has 3 lives. Each wrong move reduces one life. End game when lives become 0.
lives = 3

while lives > 0:
    move = input("Enter move (wrong/correct): ")
    if move == "wrong":
        lives -= 1
    else:
        print("Good move")

print("Game Over")