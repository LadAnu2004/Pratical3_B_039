num = []

for i in range(1, 51):
    if i % 2 == 0:
        num.append(i)

print("Even numbers Between 1 to 50:")
print(num)

min_three = num[:3]
print("Three minimum even numbers:", min_three)

max_three = num[-3:]
print("Three maximum even numbers:", max_three)

average_even = sum(num) / len(num)
print("Average of even numbers:", average_even)

