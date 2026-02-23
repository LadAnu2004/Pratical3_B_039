rows = 6
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()
#practical 4 A

rows = 5
num = 1

for i in range(rows, 0, -1):
    for j in range(i):
        print(num, end=" ")
        num += 1
        if num == 10:   # Reset after 9 
            num = 1
    print()




