# List
students = [
    ["Amit", 85, "A"],
    ["Neha", 90, "A+"],
    ["Rohit", 78, "B"],
    ["Pooja", 88, "A"]
]

#Q1.Write the code to access the first student's name.
print(students[0][0])

#Q2.Write the code to access Neha’s marks.
print(students[1][1])

#Q3.Write the code to access the grade of Rohit.
print(students[2][2])

#Q4.Write the code to print the entire second inner list.
print(students[1])

#Q5.Write the code to access Pooja’s name using negative indexing.
print(students[-1][-3])

#Q6.Write the code to access the last element of the first inner list
print(students[0][2])

#Q7.Write the code to print only the names of all students using indexing (without loop).
print(students[0][0])
print(students[1][0])
print(students[2][0])
print(students[3][0])

# print Output in single line 
print(students[0][0] ,end=" ")
print(students[1][0] ,end=" ")
print(students[2][0] ,end=" ")
print(students[3][0])