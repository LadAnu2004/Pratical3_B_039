rows = 5
for i in range(rows, 0, -1):
    for space in range(rows - i):
        print(" ", end="")
    for star in range(i):
        print("*", end=" ")
    print()
#practical 4 A

# Alphabet Pyramid (aligned perfectly)
for i in range(rows):
    print(" " * (rows - i - 1), end="")
    for j in range(i + 1):
        print(chr(65 + j), end=" ")
    print()