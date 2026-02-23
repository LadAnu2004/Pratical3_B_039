rows = 5
for i in range(rows, 0, -1):
    for space in range(rows - i):
        print(" ", end="")
    for star in range(i):
        print("*", end=" ")
    print()
