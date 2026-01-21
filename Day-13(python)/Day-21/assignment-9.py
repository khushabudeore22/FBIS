# 1. Write a program to check whether a number is positive or negative.
num = int(input("Enter number: "))
if num > 0:
    print("Positive")
else:
    print("Negative")

# 2. Write a program to check if a number is greater than 100.
num=int(input("Enter a number: "))
if num>100:
    print("The Number is greater than 100")
else:
    print("The number is not grater than 100")

# 3. Write a program to check whether a given number is even or odd.
num = int(input("Enter number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 4.Write a one-line if statement to check if a number is less than 50.
num = int(input("Enter number: "))
if num < 50: print("Less than 50")

# 5. Write a program to check whether a person is eligible to vote (age ≥ 18).
vote=int(input("Enter The Age: "))
if vote>=18:
    print("The person is eligible to vote ")
else:
    print("The person is not eligible for vote")

# 6. Write a program to check whether a number is positive, negative, or zero.
num = int(input("Enter number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# 7. Write a program to check the largest of two numbers.
first=int(input("Enter first number "))
second=int(input("Enter second Number: "))
if first > second:
    print(first)
else:
    print(second)

# 8. Write a program to check the largest of three numbers using if-elif.
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
third = int(input("Enter third number: "))
if first > second and first > third:
    print("Largest number is :", first)
elif second > third:
    print("Largest number is :", second)
else:
    print("Largest number is :", third)

# 9. Write a program to check whether a year is a leap year.
year = int(input("Enter year: "))
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a Leap year")
else:
    print(f"{year} is Not a leap year")

# 10. Write a program to check if a student passed or failed (marks ≥ 40).
marks=int(input("Enter a marks: "))
if marks>=40:
    print("Student is pass")
else:
    print("Student is Fail")

# 11. Write a program to assign grades:
#        ≥90 → A
#        ≥75 → B
#        ≥60 → C
#        Else → Fail
marks=int(input("Enter the marks: "))
if marks>=90:
    print("You Got 'A' Grade")
elif marks>=75:
    print("You Got 'B' Grade")
elif marks>=60:
    print("You Got 'C' Grade")
else:
    print("You Are Fail")

# 12. Write a program to check whether a number lies between 10 and 50 using and.
num = int(input("Enter number: "))
if num >= 10 and num <= 50:
    print("Between 10 and 50")
else:
    print("Not in range")

# 13. Write a program to check whether at least one condition is true using or.
num=int(input("Enter a number: "))
if num<0 or num>0:
    print("atleast one number is positive")

# 14. Write a program to check login:
#         username = "admin"
#         password = "1234"
username=input("Enter Username: ")
password=input("Enter password: ")
if username == "admin" and password == "1234":
    print("Login Successfully")
else:
    print("invalid password")

# 15. Write a program to check if a number is divisible by 3 and 5.
num=int(input("Enter Number: "))
if num % 3==0 and num % 5==0:
    print("The number is divisable by zero")
else:
    print("The number is not divisable by zero")

# 16. Write a nested if program to check:
#         gender = female
#         age ≥ 18 → Can vote
gender = input("Gender: ")
age = int(input("Age: "))
if gender == "female":
    if age >= 18:
        print("Can vote")
    else:
        print("Cannot vote")

# 17. Write a program to check whether a character is a vowel or consonant.
ch = input("Enter character: ")
if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
    print("Vowel")
else:
    print("Consonant")

# 18. Write a one-line if-else to check pass/fail.
marks = int(input("Enter The Marks: "))
print("Pass" if marks >= 40 else "Fail")

# 19. Write a program using not operator to reverse a condition.
num = int(input("Enter number: "))
if not num > 0:
    print("Number is not positive")
else:
    print("Number is Negative")

# 20. Write a program that uses pass inside an if block and print “Thank you” in else.
num=int(input("Enter The number: "))
if num<0:
    pass
else:
    print("Thank You")

# 21. Write a program using match to print the day name for numbers 1–7.
day=int(input("Enter a Day: "))
match day:
    case 1:print("Monday")
    case 2:print("Tuesday")
    case 3:print("Wednesday")
    case 4:print("Thursday")
    case 5:print("Friday")
    case 6:print("Saturday")
    case 7:print("Sunday")

# 22. Write a program using match to build a simple calculator (+, -, *, /).
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
op = input("Operator: ")
match op:
    case "+": print(a + b)
    case "-": print(a - b)
    case "*": print(a * b)
    case "/": print(a / b)

# 23. Write a program to categorize age:
#         <13 → Child
#         13–19 → Teen
#         20–59 → Adult
#         60+ → Senior
age = int(input("Enter Age:"))
if age < 13:
    print("Child")
elif age <= 19:
    print("Teen")
elif age <= 59:
    print("Adult")
else:
    print("Senior")

# 24. Write a program using match to check month name from month number.
month = int(input("Enter the Month Number: "))
match month:
    case 1: print("January")
    case 2: print("February")
    case 3: print("March")
    case 4: print("April")
    case 5: print("May")
    case 6: print("June")
    case 7: print("July")
    case 8: print("August")
    case 9: print("September")
    case 10: print("October")
    case 11: print("November")
    case 12: print("December")

# 25. Write a program using a match with a default case and print “Month number is not present”.
month = int(input("Enter the month number:"))
match month:
    case 1: print("January")
    case 2: print("February")
    case 3: print("March")
    case 4: print("April")
    case 5: print("May")
    case 6: print("June")
    case 7: print("July")
    case _:
        print("Month number is not present")

# 26. Write a program to check traffic signal colors and print actions.
signal=input("Enter a signal color: ")
if signal=="red":
    print("Stop")
elif signal=="yellow":
    print("Wait")
elif signal=="green":
    print("Go...")

# 27. Write a program using match to classify student group based on name list.
name = input("Enter name: ")
match name:
    case "khushi" | "neha" | "Sneha":
        print("Group A")
    case "amit" | "virat":
        print("Group B")
    case _:
        print("No group")

# 28. Write a program to check eligibility for a job:
#         Age ≥ 21
#         Degree = Yes
#         Experience ≥ 1 year
age = int(input("Age: "))
degree = input("Degree (Yes/No): ")
exp = int(input("Experience: "))
if age >= 21 and degree == "Yes" or degree=="yes" and exp >= 1:
    print("Eligible for job")
else:
    print("Not eligible for job")

# 29. Write a program using match with multiple values in one case.
num = int(input("Enter A Number:"))
match num:
    case 1|3|5:
        print("odd values")
    case 2|3|6:
        print("Even Values")
    case _:
        print("Other Number")