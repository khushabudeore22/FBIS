# Arithmatic Operations in Python
# Addition of two numbers
a=4
b=5
c=a+b
print("The addition is:",c)

# substraction of two numbers
c=a-b
print("The substaction is:",c)

# multiplication of two numbers
c=a*b
print("The Multiplication is:",c)

# Division of two numbers
c=a/b
print("The Divion is:",c)

# Exponentiation of two numbers
base=2
power=4
print("The Exponentiation is:",base**power)

# Modulus of two numbers
c=a%b  # To find the remainder after division
print("The Modulus is:",c)

# Floor Division of two numbers
c=a//b # To find the quotient after division
print("The Floor Division is:",c)

# taking input from user
# x=int(input("Enter First Number:"))
# y=int(input("Enter Second Number:"))
# sum=x+y
# print("The Sum is:",sum)
# sub=x-y
# print("The substratcion is:",sub)
# mul=x*y
# print("The Multiplication is:",mul)
# div=x/y
# print("The Division is:",div)


# Comparison Operators in Python
# 1)Equal to(==)
# it returns true if both the values are equal else it returns false
x=5
y=5
result=x==y
print("result:",x==y) # Method 1
print("The Equal operator result is:",result) # Method 2

# 2) Less than(<)
# it returns true if the left value is less than the right value else it returns false
result=x<y
print("The Less Than Operator result is:",result)

# 3) Greater than(>)
# it returns true if the left value is greater than the right value else it returns false
result=x>y
print("The Greater Than Operator result is:",result)

# 4)Less than or equal to(<=)
# it returns true if the left value is less than or equal to the right value else it returns false
result=x<=y
print("The Less Than or Equal to Operator result is:",result)

# 5)Greater than or equal to(>=)
# it returns true if the left value is greater than or equal to the right value else it returns false
result=x>=y
print("The Greater Than or Equal to Operator result is:",result)

# 6)Not equal to(!=)
# it returns true if both the values are not equal else it returns false
result=x!=y
print("The Not equal to opeartor result is:",result)


# Logical Operators in Python
# 1)AND Operator
# it returns true if both the conditions are true else it returns false
a=20
b=30
result=(a>10) and (b>20)
print("The Output is:",result)

# 2)OR Operator
# it returns true if at least one condition is true else it returns false
result=(a>10) or (b<20)
print("The Output is:",result)

# 3)NOT Operator
# it returns true if the condition is false else it returns false
result=not(a>10)
print("The Output is:",result)