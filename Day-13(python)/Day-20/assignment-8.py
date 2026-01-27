# 1. Create a dictionary with keys name, rollNo, and address and print it.
info ={"name":"khushi","rollno":2,"address":"satana"}
print(info)

# 2. Write a program to access and print the value of key name from a dictionary.
info ={"name":"khushi","rollno":2,"address":"satana"}
print(info["name"])
print(info["rollno"])
print(info["address"])

# 3. Create a dictionary and print its length using len().
info ={"name":"khushi","rollno":2,"address":"satana"}
print("The length of dictionary is:",len(info))

# 4. Write a program to check the type of a dictionary using type().
info ={"name":"khushi","rollno":2,"address":"satana"}
print(type(info))

# 5. Create a dictionary with two keys and print all its values.
info ={"name":"khushi","rollno":2,"address":"satana"}
print(info.values())

# 6. Create a dictionary and access values using both [] and get() methods.
info ={"name":"khushi","rollno":2,"address":"satana",'state': 'maharashtra'}
# access values using  []
print(info["name"])
print(info["rollno"])
# Access values using get() method
print(info.get("address"))
print(info.get("state"))

# 7. Write a program to add a new key-value pair to an existing dictionary.
info ={"name":"khushi","rollno":2,"address":"satana"}
info["country"]="india"
print(info)

# 8. Create a dictionary and update one value using the update() method.
info ={"name":"khushi","rollno":2,"address":"satana"}
info.update({"state":"maharashtra"})
print(info)

# 9. Write a program to remove a key using the pop() method.
info ={'name': 'khushi', 'rollno': 2, 'address': 'satana', 'state': 'maharashtra'}
info.pop("state")
print(info)

# 10. Create a dictionary and remove the last inserted item using popitem().
info ={'name': 'khushi', 'rollno': 2, 'address': 'satana', 'state': 'maharashtra'}
info.popitem()
print(info)

# 11. Write a program to print all keys using the keys() method.
info ={'name': 'khushi', 'rollno': 2, 'address': 'satana', 'state': 'maharashtra'}
print(info.keys())

# 12. Write a program to print all values using the values() method.
info ={"name":"khushi","rollno":2,"address":"satana"}
print(info.values())

# 13. Create a dictionary and print all key-value pairs using items().
info ={"name":"khushi","rollno":2,"address":"satana"}
print(info.items())

# 14. Convert a tuple of key-value pairs into a dictionary using dict().
info=(("name","khushi"),("rollno",2),("state","maharashtra"))
tupletodict=dict(info)
print(tupletodict)

# 15. Write a program to check if a key exists in a dictionary.
info ={"name":"khushi","rollno":2,"address":"satana"}
key=input("Enter the key: ")
if key in info:
    print("Key is present")
else:
    print("key is not present")

# 16. Create a dictionary with duplicate keys and print the output.
info ={"name":"khushi","rollno":2,"address":"satana","name2":"khushi","name3":"khushi"}
print(info)

# 17. Write a program to delete a specific key using the del keyword.
info ={"name":"khushi","rollno":2,"address":"satana"}
del info["address"]
print(info)

# 18. Write a program to delete the entire dictionary using del.
info ={"name":"khushi","rollno":2,"address":"satana"}
del info
print(info)

# 19. Create a dictionary and empty it using the clear() method.
info ={"name":"khushi","rollno":2,"address":"satana"}
info.clear()
print(info)

# 20. Copy a dictionary using the copy() method and show both dictionaries.
info ={"name":"khushi","rollno":2,"address":"satana"}
info2=info.copy()
print(info)
print(info2)

# 21. Copy a dictionary using the dict() constructor and modify the original dictionary.
info ={"name":"khushi","rollno":2,"address":"satana"}
info2=dict(info)
info["state"]="maharashtra"
print(info)
print(info2)

# 22. Write a program to demonstrate why dict1 = dict2 is not a proper copy.
dict1 = {"name":"khushi","rollno":2,"address":"satana"}
dict2 = dict1
dict2["age"] = 21
print("dict1:", dict1)
print("dict2:", dict2)

# 23. Create a dictionary and add multiple items using assignments.
dict={}
dict["name"]="khushi"
dict["age"]=21
dict["state"]="maharashtra"
dict["address"]="satana"
print(dict)

# 24. Write a program to remove multiple keys one by one using pop().
dict1 = {"name":"khushi","rollno":2,"address":"satana"}
dict1.pop("name")
dict1.pop("rollno")
dict1.pop("address")
print(dict1)

# 25. Use fromkeys() to create a dictionary with default values.
dict1={"name":"khushi","rollno":2,"address":"satana"}
print(dict1.fromkeys("name"))

# 26. Write a program to access a missing key using get() without error.
dict1={"name":"khushi","rollno":2,"address":"satana"}
dict1.get("state")
print(dict1)

# 27. Create a dictionary and print key-value pairs in tuple form.
dict1={"name":"khushi","rollno":2,"address":"satana"}
dicttotuple=tuple(dict1.items())
print(dicttotuple)

# 28. Write a program to update multiple values using update().
dict1={"name":"khushi","rollno":2,"address":"satana"}
dict1.update({"state":"maharashtra","age":21})
print(dict1)

# 29. Create a dictionary and check membership of a key using in.
dict1={"name":"khushi","rollno":2,"address":"satana"}
print("name" in dict1)

# 30. Write a program that creates a dictionary from tuples and accesses values using keys.
tuple=(("name","khushi"),("age",21),("city","satana"))
tupletdict=dict(tuple)
print(tupletdict.keys())