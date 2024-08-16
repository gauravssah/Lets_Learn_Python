# 2. Write a program to accept marks of 6 students and display them in a sorted 
# manner.

studentMarks = []

for i in range(6):
    marks = int(input(f"Enter The Marks of student No. {i} : "))
    studentMarks.append(marks)

studentMarks.sort()
print(studentMarks)
