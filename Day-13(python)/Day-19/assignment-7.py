# # append() 
# # 1. Write a program to add 10 user-entered integers into a list using append(). 
# list = []
# for i in range(10):
#     num= int(input("Enter Numbers:"))
#     list.append(num)
#     print(list)

# # 2. Append only even integers from 1 to 20 into a list. 
# even_list = []
# for i in range(1, 21):
#     if i % 2 == 0:
#         even_list.append(i)
# print(even_list)

# # 3. Append the square of each integer from an existing list into a new list. 
# nums = [1, 2, 3, 4, 5]
# square = []
# for n in nums:
#     square.append(n * n)
# print(square)

# # 4. Take integer input until the user enters `0` and append each value to a list. 
# lst = []
# while True:
#     num = int(input("Enter number: "))
#     if num == 0:
#         break
#     lst.append(num)
# print(lst)

# # 5. Append elements of a tuple `(5, 10, 15)` one by one into a list. 
# tpl = (5, 10, 15)
# lst = []
# for i in tpl:
#     lst.append(i)
# print(lst)



# # clear() 
# # 1. Write a program to clear all elements from an integer list. 
# list=[21,2,34,64,123,76,35,87,54]
# result=list.clear()
# print(result)

# # 2. Clear a list only if it contains more than 5 integers. 
# list=[21,2,34,64,123,76,35,87,54]
# if len(list) > 5:
#     result=list.clear()
# print(list)

# # 3. Display all elements of a list and then clear it. 
# list=[21,2,34,64,123,76,35,87,54]
# print(list)
# result=list.clear()
# print(result)

# # 4. Clear a list and then add 3 new integer values to it. 
# list=[21,2,34,64,123,76,35,87,54]
# result=list.clear()
# print(result)
# list.append(10)
# list.append(20)
# list.append(30)
# print(list)

# # 5. Clear a list inside a function and print the list outside the function. 
# def clear_list(mylist):
#     mylist.clear()
# list=[10,20,30,40,50]
# clear_list(list)
# print(list)


# # copy() 
# # 1. Copy all elements of one integer list into another list using copy(). 
# list1=[10,20,30,40,50]
# list2 =list1.copy()
# print("Original List:",list1)
# print("Copied List:",list2)

# # 2. Copy a list and add new integers to the copied list without affecting the original. 
# list1=[10,20,30,40,50]
# list2 =list1.copy()
# list2.append(60)
# list2.append(70)
# print("Original List:",list1)
# print("Copied List:",list2)

# # 3. Copy a list and remove an element from the copied list. 
# list1=[10,20,30,40,50]
# list2 =list1.copy()
# list2.remove(30)
# print("Original List:",list1)
# print("Copied List:",list2)

# # count() 
# # 1. Count how many times the integer 5 appears in a list. 
# list = [1,2,4,5,8,3,5,9,5]
# result=list.count(5)
# print(result)

# # 2. Count the occurrences of a user-entered integer in a list. 
# numbers=[]
# num=int(input("Enter how many elements you want to enter:"))
# for i in range(num):
#     value=int(input("Enter integer:"))
#     numbers.append(value)
# search_count = int(input("Enter the number to count: "))
# count = numbers.count(search_count)
# print(search_count, "appears", count, "times in the list")

# # 3. Count how many times an even number appears in a list. 
# numbers=[10,2,3,45,6,57,34,39,98,6,78,80]
# count=0
# for num in numbers:
#     if num % 2 == 0:
#         count += 1
# print(f"Even Numbers appear {count} times")


# # extend() 
# # 1. Extend a list with another integer list entered by the user. 
# list=[10,20,30,40,50,60]
# name=["khushi","Jayashri","Dipti","Ragini"]
# list.extend(name)
# print(list)

# # 2. Extend a list using a tuple of integers. 
# list=[10,20,30,40]
# tuple_of_integer=(50,60,70)
# list.extend(tuple_of_integer)
# print(list)

# # 3. Extend an empty list with integers from range 1 to 5. 
# list=[]
# list.extend(range(1,5))
# print(list)

# # index() 
# # 1. Find the index of a given integer in a list. 
# list=[10,20,30,40,50,60]
# print("integer index is:",list.index(30))

# # 2. Find the index of the first occurrence of integer 10 in a list. 
# list=[10,20,30,40,50,60]
# print("index of first occurence is:",list.index(10))

# # 3. Take an integer from the user and display its index in the list. 
# list=[10,20,30,40,50,60]
# num=int(input("Enter the number"))
# result=list.index(num)
# print("The Index of integer is:",result)


# # insert() 
# # 1. Insert an integer at the beginning of a list. 
# list=[1,2,3,4,5,6]
# list.insert(0,0)
# print(list)

# # 2. Insert an integer at a specific index entered by the user. 
# list=[10,20,40,60,70,80]
# num=int(input("Enter the integer:"))
# index=int(input("Enter the index: "))
# list.insert(index,num)
# print(list)

# # 3. Insert the integer 100 at index 3. 
# list=[10,20,40,60,70,80]
# list.insert(3,100)
# print(list)

# pop() 
# # 1. Remove the last integer from a list using pop(). 
# list=[10,20,40,60,70,80]
# print("Original List",list)
# list.pop(-1)
# print("after removing a element",list)

# # 2. Remove the integer at index 2 using pop(). 
# list=[10,20,40,60,70,80]
# print("Original List",list)
# list.pop(2)
# print("after removing a element",list)

# # 3. Pop all integers from a list one by one. 
# list=[1,2,3,4,5]
# for i in list[:]:
#     list.pop()
# print(list)

# # remove() 
# # 1. Remove a specific integer value from a list. 
# num=[1,2,3,4,5]
# num.remove(4)
# print(num)

# # 2. Remove the first occurrence of integer 10 from a list. 
# list=[10,20,30,40,50,60]
# list.remove(10)
# print(list)

# # 3. Remove all occurrences of a given integer from a list. 
# list=[10,20,30,40,50,60]
# result=list.remove()
# for i in list[:]:
#     list.remove()
# print(list)


# reverse() 
# 1. Reverse an integer list using reverse(). 
# 2. Reverse a list of integers without creating a new list. 
# 3. Reverse a list inside a function. 


# sort() 
# 1. Sort a list of integers in ascending order. 
# 2. Sort a list of integers in descending order. 
# 3. Sort a list and display the smallest integer.