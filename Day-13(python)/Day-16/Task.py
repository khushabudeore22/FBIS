# Task-1
stud_list=["Khushi","Jayashri","Ragini","Dipti","Anushka"]
print(stud_list)

# Task-2
stud_list=["Khushi","Jayashri","Ragini","Dipti","Anushka"]
print("The length of string is:",len(stud_list))

# Task-3
stud_list=["khushi",True,22,2.5,0,1,False]
print(stud_list[0])
print(stud_list[1])
print(stud_list[2])
print(stud_list[3])
print(stud_list[4])
print(stud_list[5])
print(stud_list[6])

# Task-4
stud_list=["Khushi","Jayashri","Ragini","Dipti","Anushka"]
print(stud_list[0])
print(stud_list[4])

# Task-5
stud_list=["Khushi","Jayashri","Ragini","Dipti","Anushka"]
print(stud_list[-1])
print(stud_list[-2])
print(stud_list[-3])
print(stud_list[-4])
print(stud_list[-5])

# Task-6
stud_list=["Khushi","Jayashri","Ragini","Dipti","Anushka"]
print("chetan" in stud_list)

# Task-7
stud_list=["Khushi","Jayashri","Ragini","Dipti","Anushka"]
stud_list[1]="Neha"
print(stud_list)

# Task-8
stud_list=[]
stud_list.append("Khushi")
stud_list.append("Payal")
stud_list.append("Prisha")
print(stud_list)

# Task-9
stud_list=["Khushi","Jayashri","Ragini","Dipti","Anushka"]
list1= stud_list.pop()
print(stud_list)

# Task-10
stud_list=["Khushi","Jayashri","Ragini","Dipti","Anushka"]
del stud_list

# Task-11
stud_list=["Khushi","Jayashri","Ragini","Dipti","Anushka","Neha","Nikita"]
print(stud_list[2:6])

# Task-12
stud_list=["Khushi","Jayashri","Ragini","Dipti","Anushka","Neha","Nikita"]
stud_list[0:2] = ["Rohit","Virat"]
print(stud_list)

# Task-13
rollno=[1,2,3,4,5]
stud_list=["Khushi","Jayashri","Ragini","Dipti","Anushka"]
list = rollno+stud_list
print(list)

# Task-14
stud_list=["Khushi","Jayashri","Ragini","Dipti","Anushka"]
stud_list.insert(3,"Neha")
print(stud_list)

# Task-15
num = [1, 2, 3]

num.extend([4, 5, 6])
print("After extending with another list:", num)

num.extend((7, 8, 9))
print("After extending with a tuple:", num)

# Task-16
stud_list=["Khushi","Jayashri","Ragini","Dipti","Anushka"]
stud_list.remove("Ragini")
print(stud_list)

# Task-17
num=[20,45,87,1,3,0,4,34,234,65]
num.sort()
print(num)

# Task-18
num=[20,45,87,1,3,0,4,34,234,65]
num.sort(reverse=True)
print(num)

# Task-19
num=[20,45,87,1,3,0,4,34,234,65,897]
num.reverse()
print(num)

# Task-20
original_list = [20,45,87,1,3,0,4,34,234,65]
copied_list = original_list.copy()
original_list.append(897)
print("Original List:", original_list)
print("Copied List:", copied_list)

# Task-21
stud_list=["Khushi","Jayashri","Ragini","Dipti","Anushka"]
rollno={"Neha":20,"Nikita":30}
stud_list.extend(rollno)
print(stud_list)

# Task-22
stud_list=["Khushi","Jayashri","Ragini","Dipti","Anushka"]
list = stud_list
stud_list.append("Neha")
print("List1:", stud_list)
print("List2:", list)

# Task-23
stud_list=["Khushi","Jayashri","Ragini","dipti","anushka","Neha","Amit","nikita"]
stud_list.sort()
print(stud_list)

# Task-24
stud_list=["Khushi","Jayashri","Ragini","dipti","anushka","Neha","Amit","nikita"]
stud_list.sort(key=str.lower)
print(stud_list)

# Task-25
stud_list=["Khushi","Jayashri","Ragini","dipti","anushka","Neha","Amit","nikita"]
stud_list.pop(4)
print(stud_list)

# Task-26
stud_list=["Khushi","Jayashri","Ragini","dipti","anushka","Neha","Amit","nikita"]
del stud_list[3] 
print(stud_list) 

# Task-27
num=[2,6,4,3,2,3,8,7,5,2]
result=num.count(2)
print(result)

# Task-28
stud_list=["Khushi","Jayashri","Ragini","Dipti","Anushka"]
result=stud_list.index("Jayashri")
print(result)

# Task-29
stud_list=["Khushi","Jayashri","Ragini"]
stud_set = {"Dipti","Anushka"}
stud_list.extend(stud_set)
print(stud_list)

# Task-30
stud_list=["Khushi","Jayashri","Ragini","Dipti","Anushka"]

stud_list.append("Neha")
print("After append:", stud_list)

stud_list.insert(2, "Nikita")
print("After insert:", stud_list)

stud_list.remove("Anushka")
print("After remove:", stud_list)

stud_list.sort()
print("After sort:", stud_list)

stud_list.reverse()
print("After reverse:", stud_list)