# 1. Create a tuple with three fruits and print it.
fruits = ("apple", "banana", "mango")
print(fruits)

# 2. Create a tuple with one item *Python*  and print its type.
fruits = ("Python",)
print(type(fruits))

# 3. Create a tuple of five numbers and print its length using *len()* .
numbers = (1, 2, 3, 4, 5)
print(len(numbers))

# 4. Create a tuple and print its first element using indexing.
num = (10, 20, 30)
print(num[0])

# 5. Create a tuple and print its last element using negative indexing.
num = (10, 20, 30)
print(num[-1])

# 6. Create a tuple using the *tuple()* constructor with values 1 to 5 and print it.
num = tuple(range(1, 6))
print(num)

# 7. Given *t = (10, 20, 30, 40, 50)* , print elements at index 1 and 3.
t = (10, 20, 30, 40, 50)
print(t[1], t[3])

# 8. Given *t = ("a","b","c","d","e")* , print elements from index 1 to 4 using slicing.
t = ("a", "b", "c", "d", "e")
print(t[1:4])

# 9. From a tuple *t = (5,10,15,20,25,30)* , print elements from index 2 to end.
t = (5, 10, 15, 20, 25, 30)
print(t[2:])

# 10. From a tuple *t = (5,10,15,20,25,30)* , print elements from start to index 3.
t = (5, 10, 15, 20, 25, 30)
print(t[:3])

# 11. Create a tuple with mixed data types (int, float, string, boolean) and print it.
t = (10, 3.14, "Python", True)
print(t)

# 12. Check whether *Python* exists in a given tuple and print the result.
t = ("Java", "Python", "C")
print("Python" in t)

# 13. Convert a tuple to a list, add a new element, and print the updated list.
t = (1, 2, 3)
lst = list(t)
lst.append(4)
print(lst)

# 14. Convert a list back into a tuple and print it.
lst = [1, 2, 3, 4]
t = tuple(lst)
print(t)

# 15. Create two tuples and concatenate them using *+=* operator.
t1 = (1, 2)
t2 = (3, 4)
t1 += t2
print(t1)

# 16. Convert a tuple to list, change the second element, and convert back to tuple.
t = (10, 20, 30)
lst = list(t)
lst[1] = 99
t = tuple(lst)
print(t)

# 17. Create a tuple and access elements using both positive and negative indexing.
t = (10, 20, 30, 40)
print(t[1])
print(t[-2])

# 18. Create a tuple of 7 elements and print its middle element.
t = (1, 2, 3, 4, 5, 6, 7)
print(t[len(t)//2])

# 19. Create a tuple and try to change one value directly (observe and write the error).
t = (1, 2, 3)
t[0] = 10

# 20. Write a program that takes a tuple, converts it to list, replaces the last element, and converts back to tuple.
t = (1, 2, 3)
lst = list(t)
lst[-1] = 99
t = tuple(lst)
print(t)

# 21. Create a tuple of 10 numbers and extract the middle 5 elements using slicing.
t = (1,2,3,4,5,6,7,8,9,10)
print(t[2:7])

# 22. Write a program to check if a value exists in a tuple before accessing its index.
t = (10, 20, 30)
value = 20
if value in t:
    print(t.index(value))
else:
    print("Value not found")

# 23. Create a tuple, convert it to list, remove one item, and convert it back to tuple.
t = (1, 2, 3)
lst = list(t)
lst.remove(2)
t = tuple(lst)
print(t)

# 24. Write a program that accepts a tuple, converts it to list, inserts a value at index 2, and converts back to tuple.
t = (1, 2, 4)
lst = list(t)
lst.insert(2, 3)
t = tuple(lst)
print(t)

# 25. Create a tuple and demonstrate slicing with positive and negative indexes in one program.
t = (10, 20, 30, 40, 50)
print(t[1:4])
print(t[-4:-1])

# 26. Write a complete program that :-
# * creates a tuple
# * prints its length
# * accesses elements
# * slices it
# * converts to list
# * updates a value
# * converts back to tuple
t = (10, 20, 30, 40)
print(len(t))
print(t[1])
print(t[:3])
lst = list(t)
lst[1] = 99
t = tuple(lst)
print(t)

# 27. Write a program that takes two tuples, adds them, and prints the final result.
t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)

# 28. Create a tuple, delete it using *del* , and then try to print it (observe the error).
t = (1, 2, 3)
del t
print(t)

# 29. A school stores a student’s basic details in a tuple because the data should not be changed accidentally.
#        The tuple contains: *student = ("Rahul", 10, "A", 85.5)*
#        *Write a program to:*
# 1. Print the student’s name and class using indexing.
# 2. Check whether "A" exists in the tuple.
# 3. Convert the tuple into a list, change the marks (85.5 → 90.0), and convert it back into a tuple.
# 4. Print the final updated tuple.
student = ("Rahul", 10, "A", 85.5)
print(student[0], student[1])
print("A" in student)
lst = list(student)
lst[3] = 90.0
student = tuple(lst)
print(student)

# 30. A customer’s selected product prices are stored in a tuple:
#       *prices = (250, 500, 750, 1000, 1250)*
#        Write a program to:
# 1. Print the total number of items using len().
# 2. Print the first and last price using positive and negative indexing.
# 3. Extract the middle three prices using slicing.
# 4. Convert the tuple into a list, add a new price 1500, and convert it back into a tuple.
# 5. Print the final tuple.
prices = (250, 500, 750, 1000, 1250)
print(len(prices))
print(prices[0], prices[-1])
print(prices[1:4])
lst = list(prices)
lst.append(1500)
prices = tuple(lst)
print(prices)