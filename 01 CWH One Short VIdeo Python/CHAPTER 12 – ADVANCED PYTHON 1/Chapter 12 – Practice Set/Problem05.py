# 5. Store the multiplication tables generated in problem 3 in a file named Tables.txt.

n = int(input("Enter a number : "))
table = [i*n for i in range(1, 11) ]

with open(f"Table_of_{n}.txt", "w") as file:
    for num in table:
        file.write(str(num) + "\n")
        

