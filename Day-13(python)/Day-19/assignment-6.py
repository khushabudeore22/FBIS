# 1. Create a set with 5 integer values and print it.
name={"khushi","Neha","Nikita","Anushka","Roshani"}
print(name)

# 2. Create a set using the set() constructor from a list.
name=["khushi","Neha","Nikita","Anushka","Roshani"]
listtoset=set(name)
print(listtoset)

# 3. Create a set with duplicate values and print the result.
num={1,2,3,5,3,5,3,2,45,67,74,21,1}
print(num)

# 4. Create a set containing True and 1. Print the set.
num={1,True}
print(num)

# 5. Write a program to find the length of a set using len().
num={1,2,3,5,3,5,3,2,45,67,74,21,1}
length=len(num)
print(length)

# 6. Create a set with mixed data types and print it.
setdata = {"khushi",22,1,False,2.4,2+5j}
print(setdata)

# 7. Write a program to access set elements using a for loop.
name=["khushi","Neha","Nikita","Anushka","Roshani"]
for name in name:
    print(name)

# 8. Create an empty set and add three elements using add().
emptyset=set()
emptyset.add(10)
emptyset.add("khushi")
emptyset.add(22)
print(emptyset)

# 9. Write a program to remove an element from a set using discard().
name={"khushi","Neha","Nikita","Anushka","Roshani"}
name.discard("Roshani")
print(name)

# 10. Write a program to remove an element from a set using remove().
name={"khushi","Neha","Nikita","Anushka","Roshani"}
name.remove("Neha")
print(name)

# 11. Write a program that removes a non-existing element using discard().
name={"khushi","Neha","Nikita","Anushka","Roshani"}
name.discard(10)
print(name)

# 12. Write a program that removes a non-existing element using remove() and observe the error.
# name={"khushi","Neha","Nikita","Anushka","Roshani"}
# name.remove(30)
# print(name)

# 13. Write a program to remove a random element from a set using pop().
name={"khushi","Neha","Nikita","Anushka","Roshani"}
name.pop()
print(name)

# 14. Write a program to clear all elements from a set using clear().
name={"khushi","Neha","Nikita","Anushka","Roshani"}
name.clear()
print(name)

# 15. Write a program to delete a set completely using del.
# name={"khushi","Neha","Nikita","Anushka","Roshani"}
# del name
# print(name)

# 16. Write a program to combine two sets using union().
name={"khushi","Neha","Nikita","Anushka","Roshani"}
rollno={1,2,3,4,5}
result=name.union(rollno)
print(result)

# 17. Write a program to combine two sets using the | operator.
name={"khushi","Neha","Nikita","Anushka","Roshani"}
rollno={1,2,3,4,5}
result=name|rollno
print(result)

# 18. Write a program to update one set using another set with update().
name={"khushi","Neha","Nikita","Anushka","Roshani"}
rollno={1,2,3,4,5}
name.update(rollno)
print(name)

# 19. Write a program to join a set with a list using union().
set1 = {10, 20, 30}
list1 = [30, 40, 50]
result = set1.union(list1)
print(result)

# 20. Write a program to join three sets using union().
set1={"khushi","neha","Nikita","Anushka"}
set2={1,2,3,4}
set3={"A","B","C","D"}
result=set1.union(set2,set3)
print(result)

# 21. Write a program to find common elements between two sets using intersection().
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}
result = set1.intersection(set2)
print(result)

# 22. Write a program to find common elements between two sets using the & operator.
set1 = {10,20,30,40,50}
set2 = {20,80,70,90,60}
result = set1 & set2
print(result)

# 23. Write a program to find intersection between a set and a list using intersection().
set1={"khushi","neha","Nikita","Anushka"}
set2={"khushi",1,2,3,4}
result= set1.intersection(set2)
print(result)

# 24. Write a program to update a set using intersection_update().
set1={"khushi","neha","Nikita","Anushka"}
set2={"Anushka",1,2,3,4}
set1.intersection_update(set2)
print(set1)

# 25. Write a program to find elements present in first set but not in second using difference().
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 6}
result = set1.difference(set2)
print(result)

# 26. Write a program to find difference between two sets using the - operator.
set1={1,2,3,4,5,6,7,8}
set2={3,6,3,67,87,98}
result=set1 - set2
print(result)

# 27. Write a program to update a set using difference_update().
set1 = {1, 2, 3, 4, 5}
set2 = {2, 4}
set1.difference_update(set2)
print(set1)

# 28. Write a program to find symmetric difference using symmetric_difference().
set1={1,2,3,4,5}
set2={2,4}
result=set1.symmetric_difference(set2)
print(result)

# 29. Write a program to find symmetric difference using the ^ operator.
set1={1,2,3,4,5,6}
set2={2,4}
result=set1 ^ set2
print(result)

# 30. Write a program to perform union, intersection, difference, and symmetric difference on two sets and print all results.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}

union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set = set1.difference(set2)
symmetric_difference_set = set1.symmetric_difference(set2)

print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference (set1 - set2):", difference_set)
print("Symmetric Difference:", symmetric_difference_set)